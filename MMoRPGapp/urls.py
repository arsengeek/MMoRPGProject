from django.urls import path, include
from .views import AdvertViews, AdvertCreate

urlpatterns = [
    path('posts/', AdvertViews.as_view(),  name='news_list'),
    path('create/', AdvertCreate.as_view(), name='model_create'),
]