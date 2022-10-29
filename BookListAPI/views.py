import json
from django.shortcuts import render 
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.decorators import api_view, renderer_classes 
 # Create your views here. 
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book

# {
# "title":"Seawolf",
# "author":"Jack London"
# }

@api_view(['GET','POST']) 
def books(request): 
    return Response('list of the books', status=status.HTTP_200_OK) 

class BookList(APIView):
    def get(self, request):
        author = request.GET.get('author')
        if(author):
            return Response({"message":"list of the books by " + author}, status.HTTP_200_OK)    

        return Response({"message":"list of the books"}, status.HTTP_200_OK)
        # return Response(request.GET.get('title'), status.HTTP_200_OK)
    
    def post(self, request):
        return Response({"title":request.data.get('title')}, status.HTTP_201_CREATED)
        return Response({"message":"new book created"}, status.HTTP_201_CREATED)
        # return Response(request.data.get('title'), status.HTTP_200_OK)
        
    # def put(self, request, format=json):
    #     return Response({"message":"book updated"}, status.HTTP_200_OK)
    #     return Response(request.data.get('title'), status.HTTP_200_OK)

# class Book(APIView):
#     def get(self, request, pk):
#         return Response({"message":"single book with id " + str(pk)}, status.HTTP_200_OK)

#     def put(self, request, pk):
#         return Response({"title":request.data.get('title')}, status.HTTP_200_OK)

class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def list(self, request):
        return Response({"message":"All books with"}, status.HTTP_200_OK)
    
class Orders():
    @staticmethod
    @api_view()
    def listOrders(request):
        return Response({'message':'list of orders'}, 200)
