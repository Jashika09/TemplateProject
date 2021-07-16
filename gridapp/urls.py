from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from gridapp import views


urlpatterns = [
    path('',views.HomepageView.as_view()),
    path('fashion.html',views.FashionpageView.as_view()),
    path('Yoga.html',views.YogapageView.as_view()),
    path('food.html',views.FoodpageView.as_view()),
    path('aboutus.html',views.AboutpageView.as_view()),
    path('glyphicons.html',views.GlyphiconspageView.as_view()),
    path('contact/',views.ContactpageView.as_view()),
    path('upload/',views.UploadpageView.as_view()),
    path('sign/',views.sign,name='sign'),
    path('feedback/',views.FeedbackpageView.as_view()),

       
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


