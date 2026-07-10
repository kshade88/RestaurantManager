from django.contrib import admin
from .models import SpiritCategory, DetailCategory, Beer, Wine, Spirit, Liqueur, Ingredient, Mixer, Garnish

# Register your models here.

admin.site.register(Beer)
admin.site.register(Wine)
admin.site.register(Spirit)
admin.site.register(Liqueur)
admin.site.register(Ingredient)
admin.site.register(Mixer)
admin.site.register(Garnish)
admin.site.register(SpiritCategory)
admin.site.register(DetailCategory)