from rest_framework import serializers
from .models import Location

class LocationSerializer(serializers.ModelSerializer):
    def validate_image(self, value):
        if value and value.size > 1024 * 1024 * 2:  # Check size only if image exists
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value and value.image.width > 4096:  # Check width if image exists
            raise serializers.ValidationError('Image width larger than 4096px')
        if value and value.image.height > 4096:  # Check height if image exists
            raise serializers.ValidationError('Image height larger than 4096px')
        return value

    def validate_latitude(self, value):
        if not -90 <= value <= 90:
            raise serializers.ValidationError('Latitude must be between -90 and 90 degrees')
        return value

    def validate_longitude(self, value):
        if not -180 <= value <= 180:
            raise serializers.ValidationError('Longitude must be between -180 and 180 degrees')
        return value

    def validate_rock_drop(self, value):
        if value is not None:
            if value < 0:
                raise serializers.ValidationError('Rock drop cannot be negative')
            if value > 3000:
                raise serializers.ValidationError('Rock drop seems unreasonably high. Please verify.')
        return value

    def validate_total_height(self, value):
        if value is not None:
            if value < 0:
                raise serializers.ValidationError('Total height cannot be negative')
            if value > 5000:
                raise serializers.ValidationError('Total height seems unreasonably high. Please verify.')
        return value

    def validate_cliff_aspect(self, value):
        valid_aspects = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
        if value not in valid_aspects:
            raise serializers.ValidationError(f'Cliff aspect must be one of {", ".join(valid_aspects)}')
        return value

    def validate(self, data):
        """
        Object-level validation that checks relationships between fields
        """
        if 'rock_drop' in data and 'total_height' in data:
            if data['rock_drop'] is not None and data['total_height'] is not None:
                if data['rock_drop'] > data['total_height']:
                    raise serializers.ValidationError('Rock drop cannot be greater than total height')

        # Validate date_opened is not in the future
        if 'date_opened' in data and data['date_opened']:
            from django.utils import timezone
            if data['date_opened'] > timezone.now().date():
                raise serializers.ValidationError('Date opened cannot be in the future')

        return data

    class Meta:
        model = Location
        fields = [
            'id', 'created_at', 'updated_at', 'name', 'country',
            'longitude', 'latitude', 'rock_drop', 'total_height', 'access',
            'cliff_aspect', 'opened_by', 'date_opened', 'image'
        ]
