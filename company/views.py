from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import BannerListSerializer, AboutUsHomeSerializer
from .models import Banner, AboutUs, AboutUsGallery
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView


# Create your views here.


class BannerListView(APIView):

    def get(self, request, *args, **kwargs):
        banners = Banner.objects.all()
        if not banners.exists():
            return Response(data={'error': 'No banners found'}, status=404)
        serializer = BannerListSerializer(banners, many=True, context={'request': request})
        return Response(data=serializer.data)


class AboutUsHomeView(APIView):

    def get(self, request, *args, **kwargs):
        about_us = AboutUs.objects.last()
        serializer = AboutUsHomeSerializer(about_us, context={'request', request})
        return Response(data=serializer.data)

