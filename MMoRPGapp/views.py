from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Advert
from .forms import CreateForm

class AdvertViews(ListView):
    model = Advert
    ordering = ''
    template_name = 'listPost.html'
    context_object_name = 'posts'
    paginate_by=10


class AdvertCreate(CreateView):
    model = Advert
    form_class = CreateForm
    success_url = '/success/'
    template_name = 'createPost.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        self.form = self.request.GET, queryset
        return self.form.qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CreateForm() 
        return context