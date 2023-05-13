from rest_framework import serializers
from .models import MenuItem, Category, Cart, Order
from django.contrib.auth.models import User, Group

class GroupSerializer(serializers.ModelSerializer):
  class Meta:
    model = Group
    fields = ['id', 'name',]

class UserSerializer(serializers.ModelSerializer):
  groups = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name',
     )
  class Meta:
    model = User
    fields = ['id', 'username', 'groups']

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ['id', 'slug', 'title']

class MenuItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = MenuItem
    category = serializers.StringRelatedField()
    fields = ['id', 'title', 'price', 'featured', 'category']
    extra_kwargs = {
      'price': {'min_value': 0}
    }

class CartSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cart
    price = serializers.SerializerMethodField(method_name = 'calculate_price')
    fields = ['id', 'user', 'menuitem', 'quantity', 'unit_price', 'price']

  def calculate_price(self, unit_price:Cart, quantity:Cart):
    return unit_price * quantity

class OrderSerializer(serializers.ModelSerializer):
  class Meta:
    model = Order
    fields = ['id', 'user', 'delivery_crew', 'status', 'total', 'date']
