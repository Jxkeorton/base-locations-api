from rest_framework import generics
from base_locations_api.permissions import IsSuperUserOrReadOnly
from .models import Location
from .serializers import LocationSerializer

class LocationList(generics.ListCreateAPIView):
    """
    List all locations or create a new location if superuser.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsSuperUserOrReadOnly]


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a location. Only superusers can modify.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsSuperUserOrReadOnly]