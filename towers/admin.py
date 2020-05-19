from django.contrib import admin

# Register your models here.
from .models import Towers, Biminis, Images, TowerOrder, BiminiOrder


class TowerOrdersAdmin(admin.ModelAdmin):
    list_display = ['name', 'tower', 'qty', 'style', 'finish']
    search_fields = ['name', 'tower', 'qty', 'style', 'finish']
    list_per_page = 25

class TowersAdmin(admin.ModelAdmin):
    list_display = ('title', 'manufacturer', 'start_year', 'end_year', 'model', 'price')
    list_display_links = ('title', 'manufacturer', 'model')
    list_filter = ('manufacturer', 'model')
    search_fields = ('title', 'manufacturer', 'start_year', 'end_year', 'model')
    list_per_page = 25


class BiminisAdmin(admin.ModelAdmin):
    list_display = ('name', 'tower', 'price')
    list_filter = ('tower',)
    search_fields = ('name', 'tower')
    list_per_page = 25

admin.site.register(Towers, TowersAdmin)
admin.site.register(Images)
admin.site.register(Biminis, BiminisAdmin)
admin.site.register(TowerOrder, TowerOrdersAdmin)
admin.site.register(BiminiOrder)

