from api.models import Creator, Demand, Video
from authentication.serializers import UserSerializer
from rest_framework import serializers

class DemandSerializer(serializers.ModelSerializer):
    demandeur_info = UserSerializer(source="demandeur", read_only=True)
    class Meta:
        model = Demand
        fields = '__all__'

class CreatorSerializer(serializers.ModelSerializer):
    total_videos = serializers.IntegerField(read_only=True)
    video_links = serializers.ListField(child=serializers.URLField(), read_only=True)

    class Meta:
        model = Creator
        fields = ['id','first_name', 'last_name', 'description', 'integration_date', 'rating', 'total_videos', 'video_links']


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'