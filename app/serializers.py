# products/serializers.py

from rest_framework import serializers
from .models import Product, Category, DeliveryInfo
from django.contrib.auth import get_user_model
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'details', 'price', 'image', 'category']

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'products']

User = get_user_model()

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
class DeliveryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryInfo
        fields = '__all__'
