from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, filters
from base_locations_api.permissions import IsOwnerOrReadOnly
from .models import Review
from .serializers import ReviewSerializer, ReviewDetailSerializer


class ReviewList(generics.ListCreateAPIView):
    """
    List Reviews or create a review if logged in.
    """
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Review.objects.all()
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
        filters.SearchFilter,
    ]
    filterset_fields = [
        'location__name',
        'owner__username',
    ]
    ordering_fields = [
        'created_at',
        'hazard',
    ]
    search_fields = [
        'owner__username'
    ]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
    
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a review or update, delete a Review if you own it
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_classes = ReviewDetailSerializer
    queryset = Review.objects.all()