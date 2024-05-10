from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Advert, Response, User
from .forms import CreateForm, ResponseForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from .filter import PostFilter
from django.core.mail import send_mail, mail_admins

class AdvertViews(ListView):
    model = Advert
    ordering = ''
    template_name = 'listPost.html'
    context_object_name = 'posts'
    paginate_by=100


class AdvertCreate(LoginRequiredMixin, CreateView):
    model = Advert
    form_class = CreateForm
    success_url = '/mmorpg/posts/'
    template_name = 'createPost.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        self.form = self.request.GET, queryset
        return self.form.qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CreateForm() 
        return context
    
    
class CommentCreate(LoginRequiredMixin, CreateView):
    model = Response
    form_class = ResponseForm
    success_url = '/mmorpg/posts/'
    template_name = 'createComment.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['post_id']
        response = super().form_valid(form)
        return response
    
    def send_email_notification(self, response):
        post = response.post
        post_author = post.author
        author = response.author
        comment = response.text
        
        send_mail(
            subject='New Comment',
            message=f'{author.username} - {comment}',
            recipient_list=[post_author.email],
            from_email=None,
        )
        
class CommetsSearch(LoginRequiredMixin, ListView):
    model = Response
    ordering = ''
    template_name = 'CommentsPost.html'
    context_object_name = 'comments'
    paginate_by=10

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Response.objects.filter(post__author_id=self.request.user.id)
        context['filter'] = PostFilter(self.request.GET, queryset, request=self.request.user.id)
        return context