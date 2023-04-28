from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet,GenericViewSet,ModelViewSet
from api.serializers import UserSerializer,JobSerializer,ProfileSerializer
from rest_framework.mixins import CreateModelMixin
from rest_framework.generics import GenericAPIView
from Service.models import Userprofile,Job,Reviews,AssignedWorks,Notification,Category
from rest_framework import authentication,permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.authtoken.views import ObtainAuthToken



class UsersView(GenericViewSet,CreateModelMixin):
    serializer_class=UserSerializer
    queryset=User.objects.all()


class ProfileView(ModelViewSet):
    serializer_class=ProfileSerializer
    queryset=Userprofile

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    
    def destroy(self, request, *args, **kwargs):
        prof=self.get_object()
        if prof.user != request.user:
            raise serializers.ValidationError("not allowed to perform")
        else:
            return super().destroy(request,*args,**kwargs)
    
    



class JobView(ModelViewSet):
    serializer_class=JobSerializer
    queryset=Job.objects.all()
    # authentication_classes=[authentication.TokenAuthentication]
    # permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    def destroy(self, request, *args, **kwargs):
        jbs=self.get_object()
        if jbs.user != request.user:
            raise serializers.ValidationError("not allowed to perform")
        else:
            return super().destroy(request,*args,**kwargs)