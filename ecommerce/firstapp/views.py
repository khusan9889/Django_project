from django.http import HttpResponse
from django.shortcuts import render
from .models import *       #importing model from db
from django.contrib.auth.decorators import login_required #login

# Create your views here.
# def second(reques):
#     return HttpResponse("<h1>That's second page</h1>")



#Connection to templates
menu = ['about site', 'add content' , 'feedback', 'enter']


def index(request):
    posts = Tutorial.objects.all()
    return render(request, 'firstapp/index.html', {'posts': posts, 'menu':menu, 'title':'Main page'})

def about(request):
    return render(request, 'firstapp/about.html', {'menu':menu,'title':'about site'})


@login_required
def profile(request):
    return render(request, 'firstapp/profile.html')

    