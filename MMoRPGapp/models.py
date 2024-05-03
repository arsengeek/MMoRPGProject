from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Advert(models.Model):
    title = models.CharField(max_length=50)
    text = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    response = models.ForeignKey('Responce', on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return f"{self.title} - {self.text}"
    
class Responce(models.Model):
    response_post_text = models.CharField(max_length=100)
    
class Categories(models.Model):
    category_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category_name