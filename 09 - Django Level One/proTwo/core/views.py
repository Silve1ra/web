from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse('HOME PAGE')
    home_dict={'home_var':'HOME PAGE'}
    return render(request, 'core/home.html', context=home_dict)

def help(request):
    help_dict={'help_var':'HELP PAGE'}
    return render(request, 'core/help.html', context=help_dict)

def contact(request):
    contact_dict={'contact_var':'CONTACT PAGE'}
    return render(request, 'core/contact.html', context=contact_dict)