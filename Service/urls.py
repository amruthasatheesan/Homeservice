from django.urls import path
from Service import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    
    path("register/",views.SignupView.as_view(),name="register"),
    path("login",views.SignInView.as_view(),name="signin"),
    path("index",views.IndexView.as_view(),name="index"),
    path("profiles/add",views.UserProfileCreateView.as_view(),name="profile-add"),
    path("profiles/detail",views.ProfileDetailView.as_view(),name="profile-detail"),
    path("profiles/<int:pk>/edit",views.ProfileUpdateView.as_view(),name="profile-edit"),
    path("signout",views.SignoutView.as_view(),name="logout"),
    path("add/job",views.JobView.as_view(),name="job-add"),
    path("job/<int:pk>/remove",views.JobDeleteView.as_view(),name="job-delete"),
    path("review/add",views.ReviewCreateView.as_view(),name="review-create"),

 

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


