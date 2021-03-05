from .models import SongModel
from rest_framework import serializers

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model=SongModel
        fields="__all__"
