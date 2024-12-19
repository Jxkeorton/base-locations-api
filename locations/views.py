from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count
from rest_framework import generics, filters
from base_locations_api.permissions import IsSuperUserOrReadOnly
from .models import Location
from .serializers import LocationSerializer

class LocationList(generics.ListCreateAPIView):
    """
    List all locations or create a new location if superuser.
    """
    serializer_class = LocationSerializer
    permission_classes = [IsSuperUserOrReadOnly]
    queryset = Location.objects.annotate(
        reviews_count=Count('review', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'country',
    ]
    ordering_fields = [
    'created_at',
    'reviews_count',
    ]
    search_fields = [
        'name',
        'country'
    ]


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a location. Only superusers can modify.
    """
    queryset = Location.objects.annotate(
        reviews_count=Count('review', distinct=True)
    )
    serializer_class = LocationSerializer
    permission_classes = [IsSuperUserOrReadOnly]
    
    def perform_update(self, serializer):
        instance = serializer.save()
        print(f"Updated Location: {instance}")