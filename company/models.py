from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import Media
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Banner(models.Model):
    title = models.CharField(_('title'), max_length=255)
    subtitle = models.CharField(_('subtitle'), max_length=255)
    bg_image = models.OneToOneField(Media, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = _('banner')
        verbose_name_plural = _('banner')


class AboutUs(models.Model):
    desc = models.TextField(_('description'))
    video = models.OneToOneField(Media, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.desc

    class Meta:
        verbose_name = _('About Us')
        verbose_name_plural = _('About US')


class AboutUsGallery(models.Model):
    image = models.OneToOneField(Media, blank=True, null=True, on_delete=models.SET_NULL)
    about_us = models.OneToOneField(AboutUs, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.about_us}-{self.image.file.url}"

    class Meta:
        verbose_name = _('About Us Gallery')
        verbose_name_plural = _('About Us')


class Contacts(models.Model):
    address = models.TextField(_('address'))
    phonenumber1 = PhoneNumberField(_('phone number1'))
    phonenumber2 = PhoneNumberField(_('phone number2'))
    work_time = models.CharField(_('work time'), max_length=255)


    def __str__(self):
        return f"{self.id}-{self.address}"


    class Meta:
        verbose_name = _('contacts')
        verbose_name_plural = _('contacts')


class SocialMedia(models.Model):
    link = models.URLField(_('link'))
    icon = models.CharField(_('icon'), max_length=255, help_text=_('write icon code'))

    def __str__(self):
        return self.link

    class Meta:
        verbose_name = _('Social Media')
        verbose_name_plural = _('Social Media')


class ContactWithUs(models.Model):
    full_name = models.CharField(_('full_name'), max_length=255)
    phone_number = models.CharField(_('phone number'), max_length=255)
    subject = models.CharField(_('subject'), max_length=255)
    message = models.TextField(_('message'))

    class Meta:
        verbose_name = _('Contact with us')
        verbose_name_plural = _('Contact with us')







