from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

class Category(models.Model):
    name=models.CharField(max_length=200,unique=True)
    
    def __str__(self):
        return self.name



class Userprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    is_active=models.BooleanField(default=True)
    profile_pic=models.ImageField(upload_to="profile",null=True,blank=True)
    skill=models.ForeignKey(Category,on_delete=models.CASCADE)
    address=models.CharField(max_length=250)
    location=models.CharField(max_length=200)
    phone_number=models.CharField(max_length=50)
    
    @property
    def review(self):
        qs=Reviews.objects.filter(product=self)
        return qs


class Job(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    description=models.CharField(max_length=350)
    skill=models.ForeignKey(Category,on_delete=models.CASCADE)
    amount=models.PositiveIntegerField()
    location=models.CharField(max_length=200)
    contact_info=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)
    options=(
        ("not-assigned","not-assigned"),
        ("assigned","assigned"),
        ("progress","progress"),
        ("finished","finished")

    )
    status=models.CharField(max_length=200,choices=options,default="not-assigned")



    
class Reviews(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    work=models.ForeignKey(Job,on_delete=models.CASCADE)
    comment=models.CharField(max_length=240)
    rating=models.FloatField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    

class AssignedWorks(models.Model):
    job=models.ForeignKey(Job,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
class Notification(models.Model):
    job=models.ForeignKey(Job,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    message=models.CharField(max_length=200)
    read_status=models.BooleanField(default=False)

