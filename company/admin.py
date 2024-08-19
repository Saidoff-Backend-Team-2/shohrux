from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    pass


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    pass


@admin.register(AboutUsGallery)
class AboutUsGalleryAdmin(admin.ModelAdmin):
    pass

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    pass

