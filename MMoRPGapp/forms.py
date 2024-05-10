from django import forms
from .models import Advert, Response

class CreateForm(forms.ModelForm):
    
    class Meta:
        model = Advert
        fields = [
            'title',
            'text',
            'categories'
        ]
        
class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['text']
