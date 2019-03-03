from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('help/', views.help, name='help'),
    path('contact/', views.contact, name='contact'),
]