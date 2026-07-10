from django import forms
from .models import Spirit, Beer, Wine, Liqueur, Mixer, Ingredient, Garnish

class SpiritForm(forms.ModelForm):
    class Meta:
        model = Spirit
        exclude = ["product"]

class BeerForm(forms.ModelForm):
    class Meta:
        model = Beer
        exclude = ["product"]

class WineForm(forms.ModelForm):
    class Meta:
        model = Wine
        exclude = ["product"]

class LiqueurForm(forms.ModelForm):
    class Meta:
        model = Liqueur
        exclude = ['product']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        exclude = ["product"]

class MixerForm(forms.ModelForm):
    class Meta:
        model = Mixer
        exclude = ['product']

class GarnishForm(forms.ModelForm):
    class Meta:
        model = Garnish
        exclude = ['product']


