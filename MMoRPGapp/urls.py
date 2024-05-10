from django.urls import path, include
from .views import AdvertViews, AdvertCreate, CommentCreate, CommetsSearch

urlpatterns = [
    path('posts/', AdvertViews.as_view(),  name='news_list'),
    path('create/', AdvertCreate.as_view(), name='model_create'),
    path('post/<int:post_id>/comment/', CommentCreate.as_view(), name='comment_create'),
    path('comments/', CommetsSearch.as_view(), name='comment_search')
]