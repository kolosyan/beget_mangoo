from django import forms
from .models import Employer


class MyModelForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'my-class'}))
    class Meta:
        model = Employer
        fields = ['name']