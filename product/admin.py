from django.contrib import admin
from .models import Product, ProductAttribute, WebOrder

# Register your models here.


@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('title', 'value', 'product')
    list_display_links = ('title', 'product')

@admin.register(WebOrder)
class WebOrder(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number')
    list_display_links = ('full_name', 'phone_number')


class ProductAttributeInline(admin.StackedInline):
    model = ProductAttribute
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductAttributeInline]
    list_display = ('title', 'desc')




