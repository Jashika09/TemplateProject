from django import forms
from gridapp.models import Register, Login, Upload
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from gridapp.models import Contact

class RegisterForm(forms.ModelForm):
    name=forms.CharField(max_length=200)
    lastname=forms.CharField(max_length=200)
    emailid=forms.CharField(max_length=200)
    password=forms.CharField(max_length=200)


    class Meta:
        model=Register
        fields=('name','lastname','emailid','password',)


class LoginForm(forms.ModelForm):
    emailid=forms.CharField(max_length=200)
    password=forms.CharField(max_length=200)


    class Meta:
        model=Login
        fields=('emailid','password',)


class SignForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','username','password1','password2')

class FileForm(forms.ModelForm):
    class Meta:
        model= Upload
        fields= ['name', 'select', 'filepath',]

class ContactForm(forms.ModelForm):
    name=forms.CharField(max_length=200)
    lastname=forms.CharField(max_length=200)
    emailid=forms.CharField(max_length=200)
    feedback=forms.CharField(max_length=200)


    class Meta:
        model=Contact
        fields=('name','lastname','emailid','feedback',)
