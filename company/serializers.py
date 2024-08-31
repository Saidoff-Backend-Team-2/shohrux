from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from .models import Banner, AboutUs, AboutUsGallery
from common.serializers import MediaURLSerializer


class BannerListSerializer(ModelSerializer):
    bg_image = MediaURLSerializer()

    class Meta:
        model = Banner
        exclude = ('id',)
        read_only_fields = ('title', 'subtitle', 'bg_image')


class AboutUsGallerySerializer(ModelSerializer):
    image = MediaURLSerializer()

    class Meta:
        model = AboutUsGallery
        fields = ('image',)


class AboutUsHomeSerializer(ModelSerializer):
    galleries = SerializerMethodField()

    class Meta:
        model = AboutUs
        fields = ('desc', 'galleries')

    def get_galleries(self, obj):
        return AboutUsGallerySerializer(obj.galleries.all(), many=True)
