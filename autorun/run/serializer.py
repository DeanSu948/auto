from rest_framework import serializers
from .models import FlashInfo

class FlashInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashInfo
        fields = "__all__"
