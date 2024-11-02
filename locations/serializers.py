from rest_framework import serializers
from .models import Location


class LocationSerializer(serializers.ModelSerializer):
    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px'
            )
        return value
    
    class Meta:
        model = Location
        fields = [
            'id', 'created_at', 'updated_at', 'name', 'country',
            'coordinates', 'rock_drop', 'total_height', 'access',
            'cliff_aspect', 'opened_by', 'date_opened', 'image'
        ]