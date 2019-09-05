from rest_framework import serializers
from .models import ProfileViewSet

class UserSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=10)


class ProfileSerializers(serializers.ModelSerializer):
    """Serializer for custom model class"""

    class Meta:
        model = ProfileViewSet
        fields = "__all__"

    def create(self, validated_data):
        """Create and return a user"""
        
        user = ProfileViewSet.objects.create(
            email= validated_data['email'],
            name= validated_data['name'],
            mobile= validated_data['mobile'],
        )
        return user