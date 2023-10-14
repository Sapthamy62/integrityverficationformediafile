from django.db import models

# Create your models here.
class UserType(models.Model):
    id= models.AutoField(primary_key=True)
    type=models.CharField(max_length=20, blank=True)    
class Actors(models.Model):

    Typeid= models.ForeignKey(UserType,models.CASCADE)
    Firstname= models.CharField(max_length=255, blank=True)
    lastname= models.CharField(max_length=255, blank=True)
    email=models.EmailField(max_length = 254)
    password=models.CharField(max_length=50)
    status=models.CharField(max_length=255, blank=True)