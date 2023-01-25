from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import Request, Response, status
from .models import File
from .serializers import FileSerializer

class FilesView(generics.ListCreateAPIView):
    def post(self, request: Request) -> Response:
        serializer = FileSerializer(data=request.data)
       
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        serializer.save()
           
        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        files = File.objects.all()

        serializer = FileSerializer(files, many=True)

        return Response(serializer.data, status.HTTP_200_OK)
