from django.db import models
from django.db.models import CheckConstraint, Q
# Create your models here.
class Document(models.Model):

    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)  
class UserType(models.Model):
    id= models.AutoField(primary_key=True)
    type=models.CharField(max_length=20, blank=True)    
class Actors(models.Model):

    Typeid= models.IntegerField()
    Firstname= models.CharField(max_length=255, blank=True)
    lastname= models.CharField(max_length=255, blank=True)
    email=models.EmailField(max_length = 254)
    password=models.CharField(max_length=50)
    status=models.CharField(max_length=255, blank=True)

