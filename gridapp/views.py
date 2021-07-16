from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from gridapp.forms import RegisterForm,SignForm, ContactForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from .models import Upload
from .forms import FileForm
from gridapp.models import Contact

#create views here

class HomepageView(TemplateView):
    template_name="home.html"
    def post(self,request):
        form= RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            text=form.cleaned_data['name']
            text=form.cleaned_data['lastname']
            text=form.cleaned_data['emailid']
            text=form.cleaned_data['password']

            form=form()
            return redirect('/')
        args={'form':form,'text':text}
        return render(request, self.template_name,args)


class FashionpageView(TemplateView):
    template_name="fashion.html"

class YogapageView(TemplateView):
    template_name="Yoga.html"

class FoodpageView(TemplateView):
    template_name="food.html"

class AboutpageView(TemplateView):
    template_name="aboutus.html"

class GlyphiconspageView(TemplateView):
    template_name="glyphicons.html"

class FeedbackpageView(ListView):
    template_name="feedback.html"
    def get_queryset(self):
        return Contact.objects.all()

class UploadpageView(TemplateView):
    template_name="upload.html"
    def showfile(request):
        lastfile= File.objects.last()
        filepath= lastfile.filepath
        filename= lastfile.name

        form= FileForm(request.post or None, request.FILES or None)
        if form.is_valid():
            form.save()

        context= {'filepath': filepath,
              'form': form,
              'filename': filename
              }
    
      
        return render(request, 'upload.html', context)

def sign(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignForm()
    return render(request, 'registration/sign.html', {'form': form})


class ContactpageView(TemplateView):
    template_name="contact.html"
    def post(self,request):
        form= ContactForm(request.POST)
        if form.is_valid():
            form.save()
            name=form.cleaned_data['name']
            lastname=form.cleaned_data['lastname']
            emailid=form.cleaned_data['emailid']
            feedback=form.cleaned_data['feedback']

            form=form()
            return redirect('/')
        args={'form':form}
        return render(request, self.template_name,args)

