from django.contrib import admin
from .models import Profile #class for profile page
# Register your models here.
from .models import *

admin.site.register(Tutorial)
admin.site.register(Profile) #Profile