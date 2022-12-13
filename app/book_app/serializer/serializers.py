from rest_framework import serializers
from book_app.models import UserProfile, Book


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        depth = 1
        exclude = ['type']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        depth = 1
        fields = '__all__'
