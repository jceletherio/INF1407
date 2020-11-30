from django import forms
from .models import Mylist

class mylistForm(forms.ModelForm):
    prefeito = forms.IntegerField(max_value=90,label='Numero do Prefeito')
    class Meta:
        model = Mylist
        fields = '__all__'