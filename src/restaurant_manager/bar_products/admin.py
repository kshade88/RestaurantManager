from django.contrib import admin
from .models import BarProduct, BeerDetail, Category, WineDetail, SpiritDetail, liqueurDetail, IngredientDetail, MixerDetail, GarnishDetail, SpiritCategory, DetailCategory

# Register your models here.
admin.site.register(BarProduct)
admin.site.register(BeerDetail)
admin.site.register(WineDetail)
admin.site.register(SpiritDetail)
admin.site.register(liqueurDetail)
admin.site.register(IngredientDetail)
admin.site.register(MixerDetail)
admin.site.register(GarnishDetail)
admin.site.register(Category)
admin.site.register(SpiritCategory)
admin.site.register(DetailCategory)