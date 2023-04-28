from django import forms
from django.contrib.auth.models import  User
from django.contrib.auth.forms import UserCreationForm

from Service.models import Userprofile,Job,Reviews


class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())

class Userprofileform(forms.ModelForm):
    class Meta:
        model=Userprofile
        fields=["profile_pic","skill","address","location","phone_number"]


class JobForm(forms.ModelForm):
    class Meta:
        model=Job
        fields=["description","location","contact_info","amount","skill"]   

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Reviews
        fields=["comment","rating"]                     