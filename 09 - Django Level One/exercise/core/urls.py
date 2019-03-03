from django.urls import path
from core import views

urlpatterns = [    
    path('', views.help, name='help'),
]