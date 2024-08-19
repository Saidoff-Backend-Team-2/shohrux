from django.contrib import admin
from .models import Product, ProductAttribute, WebOrder

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'size')
    list_display_links = ('title', 'size')


@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('title', 'value', 'size', 'product')
    list_display_links = ('title', 'product')

@admin.register(WebOrder)
class WebOrder(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number')
    list_display_links = ('full_name', 'phone_number')


