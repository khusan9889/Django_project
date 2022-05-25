from os import scandir
from xml.etree.ElementInclude import include
from django.urls import path
from .views import *


# urlpatterns = [
#     path('',index), #http://127.0.0.1:8000/
#     path('scnd/', second)
# ]

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name= 'about'),
    path('profile/', profile, name='users-profile'),

]

