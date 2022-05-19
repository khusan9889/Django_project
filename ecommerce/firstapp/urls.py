from os import scandir
from xml.etree.ElementInclude import include
from django.urls import path
from .views import *


urlpatterns = [
    path('first/',index), #http://127.0.0.1:8000/
    path('scnd/', second)
]