from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView


@api_view(['GET','POST'])
def menu(request):
    return Response('list o items on the menu',
                    status=status.HTTP_200_OK)

class MenuItems(APIView):
    def get(self, request):
        return Response({"message": "list o items on the menu"}, status=status.HTTP_200_OK)

    def post(self, request):
        return Response({"message": "new Item added at the menu"}, status=status.HTTP_201_CREATED)


class Item(APIView):
    def get(self, request, pk):
        return Response({"message": "details of item with id " + str(pk)}, status=status.HTTP_200_OK)
