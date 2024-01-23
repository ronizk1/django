from urllib import response
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from .models import Book


from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView






class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)


        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        
        # ...


        return token




class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer









class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

# Create your views here.

@api_view(['GET'])
def index(req):
    return Response('hiiiiiii')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def secret(req):
    return Response('secret')




@api_view(['GET', 'POST', 'DELETE', 'PUT', 'PATCH'])
def books(request, id=None):
    if request.method == 'GET':
        if id is not None:
            book = get_object_or_404(Book, id=id)
            serializer = BookSerializer(book)
            return Response(serializer.data)
        else:
            books = Book.objects.all()
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        print('fffffffffffffff')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        book = get_object_or_404(Book, id=id)
        book.delete()
        return Response({"message": "Book deleted successfully"}, status=204)

    elif request.method in ['PUT', 'PATCH']:
        book = get_object_or_404(Book, id=id)
        serializer = BookSerializer(book, data=request.data, partial=request.method == 'PATCH')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)