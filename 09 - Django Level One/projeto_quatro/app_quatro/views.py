from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
'''
def index(request):
    return HttpResponse("<em>Palinovic!</em>")
'''

def index(request):
    my_dict = {'insert_me':"Hello i am from views.py"}
    return render(request, 'app_quatro/index.html', context=my_dict)
    #context serve para linkar a variavel local com o index.html