from django.db import models


# Create your models here.
class User_table(models.Model):
    id = models.AutoField(primary_key=True) #automatic increament 
    username= models.CharField(max_length = 100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length = 17)
    confirm_password = models.CharField(max_length = 17)