from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from profile_api import serializers
from rest_framework import status

class HelloApi(APIView):
    serializers_class = serializers.UserSerializers
    def get(self, request):
        message = 'Hello This is our first instractoion'
        return Response({'message': message})

    def post(self, request):
        serializers = self.serializers_class(data=request.data)
        if serializers.is_valid():
            name = serializers.validated_data.get('name')
            message = "Hello {}".format(name)
            return Response({'message': message})
        else :
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
