from django import forms
from.models import *




class HomeForm(forms.ModelForm):
    class Meta:
        model = form
        fields = '__all__'