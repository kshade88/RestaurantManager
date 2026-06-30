from django.contrib import admin
from .models import BarProduct, Beer, Wine, Spirit, liqueur, Bitters

# Register your models here.
admin.site.register(BarProduct)
admin.site.register(Beer)
admin.site.register(Wine)
admin.site.register(Spirit)
admin.site.register(liqueur)
admin.site.register(Bitters)