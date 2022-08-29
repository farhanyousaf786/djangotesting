from unicodedata import name
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


#Define the home view
def home(request):
    return render(request, 'home.html', {'name': "Farhan"})


def about(request):
    return render(request, 'about.html', {'name': "Farhan"})


def base(request):
    return render(request, 'base.html', {'base': "Farhan's base"})

def add(request):
    return render(request, 'result.html', {'name': "Farhan's add"})


