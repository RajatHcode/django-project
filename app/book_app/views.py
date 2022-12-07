from django.http import JsonResponse
from book_app.serializer.serializers import UserSerializer, BookSerializer
from django.shortcuts import render
from book_app.models import UserProfile, Book
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from book_app.constants import UserType
# Create your views here.

# Views for UserProfile and Book


# End Point for the api (http://127.0.0.1:8000/api/v1/getAllUser)
# Response:
# [
#   {
#     "id": 1,
#     "type": "READER",
#     "name": "Rajesh",
#     "location": "karnal",
#     "birth_date": "1999-05-03",
#     "user": 1
# },
# {
#     "id": 2,
#     "type": "AUTHOR",
#     "name": "Raman",
#     "location": "Delhi",
#     "birth_date": "1995-03-05",
#     "user": 2
# }
# ]
@api_view(['GET'])
def usersList(request):
    users = UserProfile.objects.all()
    serialized_data = UserSerializer(users, many=True)
    return Response(serialized_data.data)


# End Point for the api (http://127.0.0.1:8000/api/v1/getAllUser/1)
# Response:
#     {
    # "id": 1,
    # "type": "READER",
    # "name": "Rajesh",
    # "location": "karnal",
    # "birth_date": "1999-05-03",
    # "user": 1
#     }
@api_view(['GET'])
def userDetail(request, pk):
    user = UserProfile.objects.get(id=pk)
    serialized_data = UserSerializer(user, many=False)
    return Response(serialized_data.data)


# End Point for the api (http://127.0.0.1:8000/api/v1/createUser)

# Payload :{
#   {
#     "type": "AUTHOR",
#     "name": "Rakesh",
#     "location": "Ambala",
#     "birth_date": "1998-03-05",
#     "user": 3
#    }

# Response :{
#           "message": "User Created Successfully!"
#           }
@api_view(['POST'])
def userCreate(request):
    serialized_data = UserSerializer(data=request.data)
    if serialized_data.is_valid():
        serialized_data.save()
        return JsonResponse({"message": "User Created Successfully!"})
    return Response(serialized_data.errors)


# End Point for the api (http://127.0.0.1:8000/api/v1/updateUser/3)

# Payload :{
#   {
#     "type": "AUTHOR",
#     "name": "Rakesh",
#     "location": "Ambala",
#     "birth_date": "1998-03-05",
#     "user": 3
#    }

# Response :{
#             "message": "User Updated Successfully!"
#           }
@api_view(['PATCH'])
def userUpdate(request, pk):
    user = UserProfile.objects.get(id=pk)
    serialized_data = UserSerializer(instance=user, data=request.data)
    if serialized_data.is_valid():
        serialized_data.save()
        return JsonResponse({"message": "User Updated Successfully!"})
    return Response(serialized_data.errors)


# End Point for the api (http://127.0.0.1:8000/api/v1/deleteUser/2)

# Response: {
#             "message": "User Deleted Successfully!"
#           }
@api_view(['DELETE'])
def userDelete(request, pk):
    user = UserProfile.objects.get(id=pk)
    user.delete()

    return JsonResponse({"message": "User Deleted Successfully!"})


# Views for Book

# End for the api is (http://127.0.0.1:8000/api/v1/getAllBooks)

# Response : [
    # {
    #     "id": 1,
    #     "name": "Wings Of Fire",
    #     "price": "330.00",
    #     "edition": 2,
    #     "link": "https://ati.dae.gov.in/ati12052021_8.pdf",
    #     "author": 2
    # },
    # {
    #     "id": 5,
    #     "name": "Ignited Minds",
    #     "price": "330.00",
    #     "edition": 2,
    #     "link": "https://wakelet.com/wake/bIBw9PCCH_C3AIbqQYKWU",
    #     "author": null
    # },
    # {
    #     "id": 6,
    #     "name": "Ignited Minds",
    #     "price": "330.00",
    #     "edition": 2,
    #     "link": "https://wakelet.com/wake/bIBw9PCCH_C3AIbqQYKWU",
    #     "author": 2
    # }
# ]
@api_view(['GET'])
def booksList(request):
    users = Book.objects.all()
    serialized_data = BookSerializer(users, many=True)
    return Response(serialized_data.data)


# End point for the api is (http://127.0.0.1:8000/api/v1/getBook/1)

# Response : {
    #     "id": 1,
    #     "name": "Wings Of Fire",
    #     "price": "330.00",
    #     "edition": 2,
    #     "link": "https://ati.dae.gov.in/ati12052021_8.pdf",
    #     "author": 2
    # }
@api_view(['GET'])
def bookDetail(request, pk):
    book = Book.objects.get(id=pk)
    serialized_data = BookSerializer(book, many=False)
    return Response(serialized_data.data)


# End point for the api is (http://127.0.0.1:8000/api/v1/createBook)

# Payload :{
#            "name": "WINGS OF FIRE",
#            "price": "113.00",
#            "edition": "2",
#            "link": "https://www.amazon.in/Wings-Fire-Autobiography-Digital-Exclusive-ebook/dp/B07F6C99Q7/ref=tmm_kin_swatch_0?_encoding=UTF8&qid=&sr="
#          }


# Response : {
#     "id": 1,
#     "name": "WINGS OF FIRE",
#     "price": "113.00",
#     "edition": 2,
#     "author": "Ramesh",
#     "link": "https://instapdf.in/rich-dad-poor-dad/",
# }
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def bookCreate(request):
    serialized_book = BookSerializer(data=request.data)
    if not serialized_book.is_valid():
        return Response(serialized_book.error_messages)

    # user that is created from django default user
    user_profile_obj = UserProfile.objects.get(user=request.user)

    if user_profile_obj.type != UserType.AUTHOR:
        return JsonResponse({"message": "Not a author"})

    serialized_book.validated_data.update({"author": user_profile_obj})
    serialized_book.save()
    return JsonResponse({"message": "Book Created Successfully"})

# End Point for the api (http://127.0.0.1:8000/api/v1/updateBook/2)

# Payload :
#     {
#     "name": "Wings Of Fire",
#     "price": "330.00",
#     "edition": 2,
#     "link": "https://ati.dae.gov.in/ati12052021_8.pdf",
#     "author": 2
#     }

# Response :{
#             "message": "Book Updated Successfully!"
#           }


@api_view(['PATCH'])
def bookUpdate(request, pk):
    book = Book.objects.get(id=pk)
    book_serialized_data = BookSerializer(instance=book, data=request.data)
    if book_serialized_data.is_valid():
        book_serialized_data.save()
        return JsonResponse({"message": "Book Updated Successfully!"})
    return Response(book_serialized_data.errors)


# End Point for this api (http://127.0.0.1:8000/api/v1/deleteBook/1)

# Resonse: {
#           "Book Deleted Successfully!"
#          }
@api_view(['DELETE'])
def bookDelete(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()

    return JsonResponse({"message": "Book Deleted Successfully!"})
