import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from account.models import CustomUser
from product.models import Product
from django.db.models import Sum

class Order(models.Model):
    class OrderStatus(models.TextChoices):
        CREATED = 'created', _('Created')
        DELIVERED = 'delivered', _('Delivered')
        CANCELLED = 'cancelled', _('Cancelled')

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_('user'), related_name="orders")
    address = models.TextField(_('address'))
    long = models.FloatField(_('longitude'), blank=True, null=True)
    lat = models.FloatField(_('latitude'), blank=True, null=True)
    status = models.CharField(_('status'), max_length=20, choices=OrderStatus.choices, default=OrderStatus.CREATED)
    phone_number = PhoneNumberField(_('phone number'))
    number = models.CharField(_('order number'), max_length=20, unique=True, null=True, blank=True)
    total_price = models.FloatField(_('total price'), blank=True, null=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.full_name}"

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def save(self, *args, **kwargs):
        total_price = self.cart_items.aggregate(Sum('subtotal_price'))['subtotal_price__sum']
        self.total_price = total_price
        self.save()

class CartItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_('user'), related_name="cart_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('product'))
    quantity = models.PositiveIntegerField(_('quantity'), default=1)
    is_visible = models.BooleanField(_('is_visible'), default=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('order'),
                              related_name='cart_items')
    subtotal_price = models.FloatField(_('subtotal price'), blank=True, null=True)
    def __str__(self):
        return f"{self.product.title} ({self.quantity})"

    class Meta:
        verbose_name = _('Cart Item')
        verbose_name_plural = _('Cart Items')


class OrderMinSum(models.Model):
    min_order_sum = models.CharField(_('minimum order sum'), max_length=255)

    def __str__(self):
        return f"Minimum order sum: {self.min_order_sum}"

    class Meta:
        verbose_name = _('Order Minimum Sum')
        verbose_name_plural = _('Order Minimum Sums')