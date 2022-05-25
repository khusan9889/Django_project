# from distutils.command.upload import upload
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

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


    # def get_absolute_url(self): #--> to show "see in website" buttom in page
    #     return reverse('about')


    class Meta:
        verbose_name = "WebGroup Team"  #change name
        verbose_name_plural = "WebGroup Team" #take out S at the end of name
        ordering = ['-time_create', 'title']

        
    
    # Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username