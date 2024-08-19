from api.models import Creator
from api.serializers import  CreatorSerializer
from rest_framework import generics

class CreatorListView(generics.ListAPIView):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer


class CreatorCreateView(generics.CreateAPIView):
    queryset = Creator.objects.all().order_by('-updated_at')
    serializer_class = CreatorSerializer


class CreatorDetailView(generics.RetrieveAPIView):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer
 