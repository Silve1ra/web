from django.shortcuts import render

# Create your views here.
def home(request):
    home_dict = {'home_var':'Pro One Home Page!'}
    return render(request, 'core/home.html', context=home_dict)

def help(request):
    help_dict = {'help_var':'Pro One Help Page!'}
    return render(request, 'core/help.html', context=help_dict)

def contact(request):
    contact_dict = {'contact_var':'Pro One Contact Page!'}
    return render(request, 'core/contact.html', context=contact_dict)