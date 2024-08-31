from django.contrib import admin

# Register your models here.

from .models import *

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'user')


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    pass