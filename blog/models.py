from django.db import models

from django.contrib.auth import get_user_model


class Article(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_image')
    description = models.TextField()
    content = models.TextField()
    dete_created = models.DateTimeField(auto_now_add=True)
    date_updated= models.DateTimeField(auto_now=True)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title

# Create your models here.
