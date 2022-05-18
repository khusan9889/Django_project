from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("<h1>First Page</h1> <br> \n\t<h3>Practising Django</h3>")
    
def second(reques):
    return HttpResponse("<h1>That's second page</h1>")