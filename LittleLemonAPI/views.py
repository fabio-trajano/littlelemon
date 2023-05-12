from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET','POST'])
def menu(request):
    return Response('list o items on the menu',
                    status=status.HTTP_200_OK)
