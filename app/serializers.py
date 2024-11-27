# products/serializers.py

from rest_framework import serializers
from .models import Product, Category, DeliveryInfo
from .models import Order, OrderItem, DeliveryInfo
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

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    delivery_info = DeliveryInfoSerializer()

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        delivery_info_data = validated_data.pop('delivery_info')
        delivery_info = DeliveryInfo.objects.create(**delivery_info_data)
        order = Order.objects.create(delivery_info=delivery_info, **validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order
