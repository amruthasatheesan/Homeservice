from django.shortcuts import render,redirect
from Service.forms import Userprofileform,LoginForm,RegistrationForm,JobForm,ReviewForm
from django.views.generic import View,CreateView,FormView,TemplateView,ListView,UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate,login,logout
from Service.models import Userprofile,Job,Reviews,AssignedWorks,Notification,Category
from django.utils.decorators import method_decorator


def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper
dectr=[signin_required,never_cache]


class SignupView(CreateView):
    model=User
    form_class=RegistrationForm
    template_name="register.html"
    success_url=reverse_lazy("signin")


class SignInView(FormView):
    template_name="login.html"
    form_class=LoginForm
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("index")
            else:
                return render(request,"login.html",{"form":self.form_class})

@method_decorator(dectr,name="dispatch")
class IndexView(TemplateView):
    template_name="index.html"

@method_decorator(dectr,name="dispatch")
class JobView(CreateView,ListView):
    model=Job
    form_class=JobForm
    template_name="job-add.html"
    success_url=reverse_lazy("index")
    context_object_name="jobs"
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    def get_queryset(self):
        return Job.objects.all().order_by("-date")

@method_decorator(dectr,name="dispatch")
class UserProfileCreateView(CreateView,ListView):
    form_class=Userprofileform
    model=Userprofile
    template_name="profile-add.html"
    success_url=reverse_lazy("index")
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    
    
@method_decorator(signin_required,name="dispatch")
class ReviewCreateView(CreateView,ListView):
    model=Reviews
    form_class=ReviewForm
    template_name="review-create.html"
    success_url=reverse_lazy("index")
    context_object_name="revw"
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    def get_queryset(self):
      return Reviews.objects.all()
        

@method_decorator(dectr,name="dispatch")
class ProfileDetailView(TemplateView):
    template_name="profile-detail.html"


@method_decorator(dectr,name="dispatch")
class ProfileUpdateView(UpdateView):
    form_class=Userprofileform
    model=Userprofile
    template_name="profile-edit.html"
    success_url=reverse_lazy("index")


@method_decorator(dectr,name="dispatch")
class SignoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")


    

@method_decorator(dectr,name="dispatch")
class JobDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Job.objects.get(id=id).delete()
        return redirect("index")