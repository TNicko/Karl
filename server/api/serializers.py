from rest_framework import serializers
from .models import Session, WebsitePage

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'

class WebsitePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebsitePage
        fields = '__all__'