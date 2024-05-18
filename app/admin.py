from django.contrib import admin
from .models import Patient
from .models import Comment
from .models import Product,Category, DeliveryInfo


# Register your models here.

admin.site.register(Patient)
admin.site.register(Comment)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(DeliveryInfo)
