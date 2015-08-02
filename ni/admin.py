from django.contrib import admin
from ni.models import Shop

class ShopOptions(admin.ModelAdmin):
    pass

admin.site.register(Shop, ShopOptions)
