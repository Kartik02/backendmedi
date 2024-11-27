
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from app.models import Patient
from rest_framework.decorators import api_view
from django.shortcuts import render
from .models import Comment
from django import forms
from .models import Comment
from .forms import ProductForm
from .models import Product, Category
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer,CategorySerializer, DeliveryInfoSerializer
from django.core.paginator import Paginator
from .serializers import UserLoginSerializer
from django.contrib.auth import authenticate, login
from .models import Order
from .serializers import OrderSerializer
# views.py

from rest_framework import generics
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer



class PatientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = (
            "name",
            "email",
            "phone",
            "city",
            "address",
            "medicine",
            "prescription",
            "definition",
        )


@api_view(["POST"])
def submit_form(request, format=None):
    serializer = PatientCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Form Submitted Successfully"}, status=status.HTTP_201_CREATED)
    else:
        print("Validation errors:", serializer.errors)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def get_prescriptions(request):
    
    patients = Patient.objects.all()
 
    serializer = PatientCreateSerializer(patients, many=True)
    
    return Response(serializer.data)

class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            
            "name",
            "comment",
        )


@api_view(["POST"])
def post_comment(request, format=None):
    if request.method == "POST":
        serializer = PostCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "comment saved  Successfully"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def get_comments(request):
    comments = Comment.objects.all()  # Fetch all comments from the database
    data = [{'name': comment.name, 'comment': comment.comment} for comment in comments]
    return JsonResponse(data, safe=False)  # Return the comments as JSON response    


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')  # Ensure ordering to maintain consistent pagination
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        print("Requested Page: ", request.query_params.get('page'))
        print("Response Data: ", response.data)
        return response

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given category,
        by filtering against a `category` query parameter in the URL.
        """
        queryset = Product.objects.all()
        category_name = self.request.query_params.get('category_name')
        if category_name is not None:
            category = Category.objects.filter(name=category_name).first()
            if category:
                queryset = queryset.filter(category=category)
        return queryset



@api_view(['POST'])
def login_view(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        user = authenticate(username=serializer.validated_data['username'],
                            password=serializer.validated_data['password'])
        if user:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def delivery_info(request):
    if request.method == 'POST':
        serializer = DeliveryInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_deliveryinfo(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    data = {
        "email": patient.email,
        "phone": patient.phone,
        "name": patient.name,
        "address": patient.address,
        "country": patient.country,
        "state": patient.state,
        "city": patient.city,
        "zipcode": patient.zipcode
    }
    return JsonResponse(data)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
