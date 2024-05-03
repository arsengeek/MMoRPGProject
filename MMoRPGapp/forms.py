from django import forms
from .models import Advert

class CreateForm(forms.ModelForm):
    
    class Meta:
        model = Advert
        fields = [
            'title',
            'text',
            
        ]