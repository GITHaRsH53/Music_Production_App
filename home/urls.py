from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'), #run index function from views.py
    path('about', views.about, name='about'), 
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'), # it tells as request comes to contact page, run contact function from views.py
]