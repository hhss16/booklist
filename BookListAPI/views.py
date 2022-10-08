import json
from django.shortcuts import render 
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.decorators import api_view 
 # Create your views here. 
from rest_framework.views import APIView

# {
# "title":"Seawolf",
# "author":"Jack London"
# }

@api_view(['GET','POST']) 
def books(request): 
    return Response('list of the books', status=status.HTTP_200_OK) 

class BookList(APIView):
    def get(self, request, format=None):
        return Response({"message":"list of the books"}, status.HTTP_200_OK)
        # return Response(request.GET.get('title'), status.HTTP_200_OK)
    
    def post(self, request, format=json):
        return Response({"message":"new book created"}, status.HTTP_201_CREATED)
        # return Response(request.data.get('title'), status.HTTP_200_OK)
        
    # def put(self, request, format=json):
    #     return Response({"message":"book updated"}, status.HTTP_200_OK)
    #     return Response(request.data.get('title'), status.HTTP_200_OK)