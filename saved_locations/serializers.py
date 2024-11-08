from rest_framework import serializers
from .models import SavedLocation

class SavedLocationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = SavedLocation
        fields = ['id', 'owner', 'location', 'created_at']