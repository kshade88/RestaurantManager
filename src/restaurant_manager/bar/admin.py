from django.contrib import admin
from .models import BeerDetail, WineDetail, SpiritDetail, liqueurDetail, IngredientDetail, MixerDetail, GarnishDetail, SpiritCategory, DetailCategory

# Register your models here.

admin.site.register(BeerDetail)
admin.site.register(WineDetail)
admin.site.register(SpiritDetail)
admin.site.register(liqueurDetail)
admin.site.register(IngredientDetail)
admin.site.register(MixerDetail)
admin.site.register(GarnishDetail)
admin.site.register(SpiritCategory)
admin.site.register(DetailCategory)