from django.db import models

# Create your models here.
class User(models.Model):
	Email = models.CharField(max_length=20, unique = True)
	Firstname = models.CharField(max_length=20)
	Lastname = models.CharField(max_length=20)
	Password = models.CharField(max_length=20)
	Phone = models.CharField(max_length=10)