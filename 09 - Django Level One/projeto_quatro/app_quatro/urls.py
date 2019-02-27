#from django.conf.urls import url
from django.urls import path
from app_quatro import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    path('', views.index, name='index'),
]