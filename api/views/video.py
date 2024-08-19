
from api.models import Video
from api.serializers import  VideoSerializer
from rest_framework import generics

class VideoListView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer