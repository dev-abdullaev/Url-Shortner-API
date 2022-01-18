from rest_framework import serializers

from .models import Link



class UrlListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['id','original_link', 'shortened_link']
        read_only_fields = ['shortened_link']



class UrlCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['id', 'original_link', 'shortened_link']
