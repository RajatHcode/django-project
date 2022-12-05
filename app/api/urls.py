from django.urls import path
from .views import UserDetailAPI, RegisterUserAPIView


urlpatterns = [
    path("get-details", UserDetailAPI.as_view()),
    path('api/v1/registerUser', RegisterUserAPIView.as_view()),
]
