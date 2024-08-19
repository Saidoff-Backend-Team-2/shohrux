from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import Media
from phonenumber_field.modelfields import PhoneNumberField


class Product(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    size = models.CharField(_('size'), max_length=255)
    image = models.OneToOneField(Media, blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return f"{self.title}/ {self.size}"


class ProductAttribute(models.Model):
    title = models.CharField(max_length=255)
    value = models.CharField(max_length=20)
    size = models.CharField(_('size'), max_length=255)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL, related_name='attributes')

    class Meta:
        verbose_name = _('Product Attributes')
        verbose_name_plural = _('Attributes of Products')

    def __str__(self):
        return f"{self.title}/ {self.size}"


class WebOrder(models.Model):
    full_name = models.CharField(_('full name'), max_length=255)
    phone_number = PhoneNumberField(_('Phone number:'))

    class Meta:
        verbose_name = _('Web Order')
        verbose_name_plural = _('Web Orders')

    def __str__(self):
        return f"{self.full_name}"
