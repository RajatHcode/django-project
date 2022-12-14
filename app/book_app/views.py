from book_app.serializer.serializers import UserSerializer, BookSerializer
from django.shortcuts import render
from book_app.models import UserProfile, Book
from rest_framework import viewsets, permissions
from rest_framework import permissions, authentication
from rest_framework.response import Response
from book_app.constants import UserType
# Create your views here.


# User API View Set
class UserAPIViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [authentication.TokenAuthentication]
    http_method_names = ["get", "post", "patch", "delete"]
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        ser_user = UserSerializer(data=request.data)
        if ser_user.is_valid():
            ser_user.validated_data.update({"user": request.user})
            ser_user.save()
            return Response({"message": "User Profile Created Successfully"})
        return Response({ser_user.errors})


# Book API View Set

class BookAPIViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [authentication.TokenAuthentication]
    http_method_names = ["get", "post", "patch", "delete"]
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        ser_book = BookSerializer(data=request.data)
        if not ser_book.is_valid():
            return Response(ser_book.errors)

        # user that is created from django default user
        user_profile_obj = UserProfile.objects.get(user=request.user)

        if user_profile_obj.type != UserType.AUTHOR:
            return Response({"message": "Not a author"})

        ser_book.validated_data.update({"author": user_profile_obj})
        ser_book.save()
        return Response({"message": "Book Created Successfully"})
