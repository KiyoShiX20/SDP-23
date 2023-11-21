from django.shortcuts import render
from django.http import HttpResponse
def display(request):
    s = '<h1> Hello Samply webpage</h1>'
    return HttpResponse(s)