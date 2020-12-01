from django import forms
from .models import Mylist

class mylistForm(forms.ModelForm):
    class Meta:
        model = Mylist
        fields = ('myprefeito',)