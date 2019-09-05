from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from profile_api import serializers
from rest_framework import status
from .models import ProfileViewSet


class HelloApi(APIView):
    serializer_class = serializers.UserSerializers
    def get(self, request):
        message = 'Hello This is our first instractoion'
        return Response({'message': message})

    def post(self, request):
        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid():
            name = serializers.validated_data.get('name')
            message = "Hello {}".format(name)
            return Response({'message': message})
        else :
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileApi_ViewSet(viewsets.ModelViewSet):
    """creating and updating viewset"""

    serializer_class = serializers.ProfileSerializers
    queryset = ProfileViewSet.objects.all()
