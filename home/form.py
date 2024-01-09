from django import forms
from .models import Tokens, Course, User

class TokenForm(forms.ModelForm):
    class Meta:
        model = Tokens
        fields = [ 'course', 'user', 'expiration_time']
        widgets = {
          
            'course': forms.Select(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
            'expiration_time': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
        }
