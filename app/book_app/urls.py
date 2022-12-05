from django.urls import path

from book_app.views import *

urlpatterns = [
    path('getAllUser', usersList, name='users'),
    path('getUser/<str:pk>/', userDetail, name='detail'),
    path('createUser', userCreate, name='create'),
    path('updateUser/<str:pk>/', userUpdate, name='update'),
    path('deleteUser/<str:pk>/', userDelete, name='delete'),
    path('getAllBooks', booksList, name="books"),
    path('getBook/<str:pk>/', bookDetail, name="detail"),
    path('createBook', bookCreate, name="create"),
    path('updateBook/<str:pk>/', bookUpdate, name="update"),
    path('deleteBook/<str:pk>/', bookDelete, name='delete'),
]
