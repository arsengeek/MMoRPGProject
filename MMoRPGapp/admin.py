from django.contrib import admin
from .models import Advert, Categories, Responce
from modeltranslation.admin import TranslationAdmin

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']

class PostAdmin(TranslationAdmin):
    model = Advert
    
class CategoryAdmin(TranslationAdmin):
    model = Categories
    
admin.site.register(Advert, ProductAdmin)
admin.site.register(Categories)