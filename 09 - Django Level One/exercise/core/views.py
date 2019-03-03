from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('home page')

def help(request):
    help_dict = {'help_insert':'Help Page'}
    return render(request, 'core/help.html', context=help_dict)