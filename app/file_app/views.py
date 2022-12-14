from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from file_app.serializers import FileUploadSerializer

# Create your views here.


class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        ser_file_data = FileUploadSerializer(data=request.data)
        if ser_file_data.is_valid():
            ser_file_data.save()
            return Response(ser_file_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser_file_data.errors, status=status.HTTP_400_BAD_REQUEST)
