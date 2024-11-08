from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import SavedLocation
from .serializers import SavedLocationSerializer

class SavedLocationList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SavedLocationSerializer

    def get_queryset(self):
        return SavedLocation.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SavedLocationDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SavedLocationSerializer
    queryset = SavedLocation.objects.all()

    def get_queryset(self):
        return SavedLocation.objects.filter(owner=self.request.user)