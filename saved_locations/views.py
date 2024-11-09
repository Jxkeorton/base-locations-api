from rest_framework import generics, permissions
from base_locations_api.permissions import IsOwnerOrReadOnly
from .models import SavedLocation
from .serializers import SavedLocationSerializer

class SavedLocationList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SavedLocationSerializer

    def get_queryset(self):
        return SavedLocation.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SavedLocationDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SavedLocationSerializer
    
    def get_queryset(self):
        return SavedLocation.objects.filter(owner=self.request.user)