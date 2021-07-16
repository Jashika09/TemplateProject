from django.db import models


# Create your models here.

class Register(models.Model):
    name=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    emailid=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

    def __str__(self):
        return name


class Login(models.Model):
    emailid=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

    def __str__(self):
        return emailid

class Upload(models.Model):
    name=models.CharField(max_length=500)
    select=models.CharField(max_length=500)
    filepath= models.FileField(upload_to='files/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.filepath)

class Contact(models.Model):
    name=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    emailid=models.CharField(max_length=200)
    feedback=models.CharField(max_length=200)

    def __str__(self):
        return name
