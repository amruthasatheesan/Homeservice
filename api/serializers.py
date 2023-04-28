from django.contrib.auth.models import User
from rest_framework import serializers
from Service.models import Userprofile,User,Job

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password"]
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


    
class ProfileSerializer(serializers.ModelSerializer):
    question_count=serializers.CharField(read_only=True)
    user=UserSerializer(read_only=True,many=False)
    class Meta:
        model=Userprofile
        fields="__all__"
        


class JobSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    created_date=serializers.DateTimeField(read_only=True)
    class Meta:
        model=Job
        fields=["id","description","image","user","created_date"]