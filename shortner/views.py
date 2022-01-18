from django.shortcuts import render,redirect

from rest_framework import generics
from django.views import View
from django.conf import settings

from .models import Link
from .serializers import UrlListSerializer, UrlCreateSerializer



class UrlListAPIView(generics.ListCreateAPIView):
    queryset = Link.objects.all()
    serializer_class = UrlListSerializer


class UrlDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Link.objects.all()
    serializer_class = UrlListSerializer



class Redirector(View):
    def get(self,request,shortener_link,*args, **kwargs):
        shortener_link=settings.HOST_URL+'/'+self.kwargs['shortener_link']
        redirect_link=Link.objects.filter(shortened_link=shortener_link).first().original_link
        return redirect(redirect_link)