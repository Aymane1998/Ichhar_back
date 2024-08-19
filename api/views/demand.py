from api.models import Demand
from api.serializers import  DemandSerializer
from rest_framework import generics, response, status, permissions

class DemandListView(generics.ListAPIView):
    queryset = Demand.objects.all()
    serializer_class = DemandSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name__in=['Administrator', 'Createur']).exists():
            # User belongs to 'Administrator' or 'Createur' group, show all demands
            return Demand.objects.all()
        else:
            # User doesn't belong to 'Administrator' or 'Createur' group, show only their demands
            return Demand.objects.filter(demandeur=user)



class DemandCreateView(generics.CreateAPIView):
    queryset = Demand.objects.all().order_by('-updated_at')
    serializer_class = DemandSerializer

    def create(self, request, *args, **kwargs):
        # Serialize the request data to create a Demand instance
        data = request.data
        data["demandeur"]= request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        demande = serializer.create(serializer.validated_data)
        return response.Response(status=status.HTTP_201_CREATED, data=self.get_serializer(demande).data)
        


class DemandUpdateView(generics.UpdateAPIView):
    queryset = Demand.objects.all().order_by('-updated_at')
    serializer_class = DemandSerializer