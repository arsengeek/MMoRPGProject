from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.http import request

class Advert(models.Model):
    title = models.CharField(max_length=50)
    text = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    response = models.ForeignKey('Response', on_delete=models.CASCADE, related_name='author_post', null=True, blank=True)
    categories = models.ForeignKey('Categories', on_delete=models.CASCADE, blank=False, null=True)
    time_post = models.DateTimeField(auto_now_add=True, blank=False, null=True)
    
    def __str__(self):
        return f"{self.title} - {self.text}"

class Response(models.Model):
    post = models.ForeignKey(Advert, on_delete=models.CASCADE, related_name='responses', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    text = models.CharField(max_length=100)
    
class Categories(models.Model):
    category_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category_name
    
# class AdvertResponse(models.Model):
#     advert = models.ForeignKey(Response, on_delete=models.CASCADE, blank=True, null=True)
#     response = models.ForeignKey(Advert, on_delete=models.CASCADE, blank=True, null=True)