from django import forms
from .models import Employer


class MyModelForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'my-class'}))
    pass_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'pass_num'}))
    class Meta:
        model = Employer
        fields = ['name', 'pass_number']