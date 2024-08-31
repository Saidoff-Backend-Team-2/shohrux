from rest_framework.serializers import Serializer
from django.conf import settings


class MediaURLSerializer(Serializer):

    def to_representation(self, obj):
        request = self.context['request']
        try:
            return request.build_absolute_uri(obj.file.url)
        except:
            return settings.HOST + obj.file.url