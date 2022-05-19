# from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Tutorial(models.Model):
    title = models.CharField(max_length=50)
    #email = models.EmailField()
    content = models.TextField(blank=True)   # --> For more info about field types in "https://metanit.com/python/django/5.2.php" 
    photo = models.ImageField(upload_to="photos/%Y/%m/%d") 
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):      #return a title name from db while running through shell
        return self.title
