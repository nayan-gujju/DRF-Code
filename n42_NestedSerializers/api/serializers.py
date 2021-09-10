from rest_framework import serializers
from .models import Singer, Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'duration', 'singer']

class SingerSerializer(serializers.ModelSerializer):
    sungby = SongSerializer(read_only = True, many=True)
    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'sungby']