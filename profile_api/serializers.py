from rest_framework import serializers

class UserSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=10)