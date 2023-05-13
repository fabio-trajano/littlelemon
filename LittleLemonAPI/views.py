from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import ManagerPermission, DeliveryCrewPermission, CustomerPermission, ReadOnlyPermission
from .models import MenuItem, Category, Cart, Order
from django.contrib.auth.models import User, Group
from .serializers import MenuItemSerializer, CategorySerializer, CartSerializer, OrderSerializer, GroupSerializer, UserSerializer

class GroupsView(generics.ListCreateAPIView):
    permissions_classes = [IsAdminUser|ManagerPermission|ReadOnlyPermission]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ManagerUsersView(generics.ListCreateAPIView):
    permissions_classes = [IsAdminUser|ManagerPermission]
    queryset = User.objects.filter(groups__name='Manager')
    serializer_class = UserSerializer


class SingleManagerUserView(generics.ListCreateAPIView):
    queryset = User.objects.filter(groups__name='Manager')
    serializer_class = UserSerializer

class SingleDeliveryCrewUserView(generics.ListCreateAPIView):
    queryset = User.objects.filter(groups__name='Delivery Crew')
    serializer_class = UserSerializer

class DeliveryCrewUsersView(generics.ListCreateAPIView):
    queryset = User.objects.filter(groups__name='Delivery Crew')
    serializer_class = UserSerializer

class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MenuItemsView(generics.ListCreateAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class CartItemsView(generics.ListCreateAPIView, generics.DestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class OrdersView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class SingleOrderView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
