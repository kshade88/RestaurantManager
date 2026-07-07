from django import forms
from .models import SpiritDetail

class SpiritDetailForm(forms.ModelForm):
    class Meta:
        model = SpiritDetail
        exclude = ["name"]

