from unicodedata import name
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


#Define the home view
def home(request):
    return HttpResponse('<h1>HELLLOOOO</h1>')


def about(request):
    return render(request, 'about.html', {'name': "Farhan"})