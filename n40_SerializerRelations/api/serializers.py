from rest_framework import serializers, views
from .models import Singer, Song

class SingerSrializer(serializers.ModelSerializer):
    # song = serializers.StringRelatedField(read_only=True, many=True)
    # song = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    # song = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='song-detail')
    # song = serializers.SlugRelatedField(read_only=True, many=True, slug_field='title')
    # song = serializers.SlugRelatedField(read_only=True, many=True, slug_field='duration')
    song = serializers.HyperlinkedIdentityField(view_name = 'song-detail')
    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'song']

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'duration', 'singer']