# import the standard Django Model 
# from built-in library
from django.db import models
from django.contrib.auth.models import User as AuthUser

# Create your models here.
# Declare a new model
class Student(models.Model):
    # Fields of the model
    fname = models.CharField(max_length=100, verbose_name='First Name')
    lname = models.CharField(max_length=100, verbose_name='Last Name')
    birthdate = models.DateField()
    subject = models.TextField()
    roll_num = models.IntegerField(unique=True)


    def __str__(self):
        return self.fname


class User(models.Model):
    user =  models.OneToOneField(AuthUser, null=True, blank=True, on_delete=models.CASCADE)
    profile_image = models.ImageField(null=True, blank=True, upload_to="profile_image/", default="noimg.png")


    def __str__(self):
        return self.user.username

    def imageUrl(self):
        try:
            url = self.profile_image.url
        except:
            url = 'noimg.png'
        return url
