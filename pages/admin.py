from django.contrib import admin

from .models import Products, Orders, Customers, Dealers, Address, Shipping, OrderDetails, Contact
# Register your models here.


class DealersAdmin(admin.ModelAdmin):
    list_display = ('name', 'dealer_of', 'contactName', 'email', 'has_ordered')
    list_display_links = ('name', 'contactName')
    list_filter = ('dealer_of', 'has_ordered')
    search_fields = ('name', 'dealer_of', 'contactName', 'email')
    list_per_page = 25

class CustomersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    list_display_links = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')
    list_per_page = 25


class AddressAdmin(admin.ModelAdmin):
    list_display = ('address1', 'city', 'zipCode', 'phone', 'date_created')
    list_display_links = ('address1', 'city')
    list_filter = ('date_created',)
    search_fields = ('address1', 'city', 'zipCode', 'phone', 'date_created')
    list_per_page = 25


class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'order', 'tower', 'bimini')
    list_display_links = ('name', 'product', 'order')
    list_filter = ('product', 'order', 'tower', 'bimini')
    search_fields = ('name', 'product', 'order', 'tower', 'bimini')
    list_per_page = 25


class ContactAdmin(admin.ModelAdmin):
    list_display = ('fullName', 'phone', 'email', 'message', 'date_created')
    list_filter = ('date_created',)
    list_per_page = 25



admin.site.register(Customers, CustomersAdmin)
admin.site.register(Dealers, DealersAdmin)
admin.site.register(Products)
admin.site.register(Orders)
admin.site.register(Address, AddressAdmin)
admin.site.register(Shipping)
admin.site.register(OrderDetails, OrderDetailsAdmin)
admin.site.register(Contact, ContactAdmin)


