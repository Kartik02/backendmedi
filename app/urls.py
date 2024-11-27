# products/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet,CategoryViewSet, login_view , delivery_info
from . import views
from .views import OrderViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login_view, name='login'),
    path('delivery/', delivery_info, name='delivery_info'),
]

