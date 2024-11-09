from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    location_name = serializers.ReadOnlyField(source='location.name')
    
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    def validate(self, attrs):
        if not attrs.get('subject'):
            raise serializers.ValidationError({'subject': 'This field is required.'})
        if not attrs.get('content'):
            raise serializers.ValidationError({'content': 'This field is required.'})
        return attrs
    
    class Meta:
        model = Review
        fields = ['id', 'owner','is_owner','location_name','profile_id', 'profile_image', 'location', 'subject', 'content', 'hazard', 'created_at', 'updated_at']


class ReviewDetailSerializer(ReviewSerializer):
    """
    Serializer for the Review model used in Detail view
    Location is a read-only field so that we don't have to set it on each update
    """
    location = serializers.ReadOnlyField(source='location.id')
    location_name = serializers.ReadOnlyField(source='location.name')
    
    class Meta:
        model = Review
        fields = ReviewSerializer.Meta.fields + ['location', 'location_name'] 
