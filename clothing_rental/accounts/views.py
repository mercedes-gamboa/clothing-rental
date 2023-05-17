from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
    s = '<h1>Hello! welcome to RentB !</h1>'
    return HttpResponse(s)