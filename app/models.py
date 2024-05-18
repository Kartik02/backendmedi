from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    address = models.TextField()
    medicine = models.CharField(max_length=100)
    prescription = models.FileField(upload_to='prescriptions')
    definition = models.TextField()
    def __str__(self):
        return self.name


    
class Comment(models.Model):
    name = models.CharField(max_length=255)
    comment = models.TextField()
    def __str__(self):
        return self.name
   

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    details = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True)
    def __str__(self):
        return self.name
    
class DeliveryInfo(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    name = models.CharField(max_length=100)
    address = models.TextField()
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    

    

