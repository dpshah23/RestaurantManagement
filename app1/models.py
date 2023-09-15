from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='img')

    def __str__(self):
        return self.name
    

class Register(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.CharField(max_length=10)
    address=models.TextField()
    password=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class Logo(models.Model):
    name=models.CharField(max_length=10)
    logo=models.ImageField(upload_to='logo')

    def __str__(self):
        return self.name