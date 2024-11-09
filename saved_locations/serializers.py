from rest_framework import serializers
from .models import SavedLocation

class SavedLocationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    location_name = serializers.ReadOnlyField(source='location.name')
    location_image = serializers.ReadOnlyField(source='location.image')
    
    class Meta:
        model = SavedLocation
        fields = [
            'id', 
            'owner', 
            'location',
            'location_name',
            'location_image', 
            'created_at'
        ]