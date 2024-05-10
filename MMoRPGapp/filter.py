from django_filters import FilterSet, ModelChoiceFilter, DateTimeFilter
from django.forms import DateTimeInput
from .models import Response, Categories, Advert

class PostFilter(FilterSet):
    
    class Meta:
        model = Response
        fields = {
            'post',

        }
        
    def __init__(self, *args, **kwargs):
        super(PostFilter, self).__init__(*args, **kwargs)
        self.filters['post'].queryset = Advert.objects.filter(author_id=kwargs['request'])
        