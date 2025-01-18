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

    def validate(self, data):
        """
        Check if the location is already saved by this user.
        """
        user = self.context['request'].user
        location = data.get('location')

        # Check for existing saved location
        if SavedLocation.objects.filter(
            owner=user, location=location
        ).exists():
            raise serializers.ValidationError({
                "location": "You have already saved this location."
            })

        return data
