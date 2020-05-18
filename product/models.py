from django.conf import settings
from django.db import models
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
class Subtag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Color(models.Model):
    color = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.color
    
class Size(models.Model):
    size = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.size

class Product(models.Model):
    CATEGORY = (
        ('indoor', 'indoor'),
        ('out door', 'out door'),
    )
    brand_name = models.CharField(max_length=200, null=True, blank=True)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
    subtag = models.ForeignKey(Subtag, on_delete=models.SET_NULL, null=True)
    p_image = models.ImageField(upload_to='products', null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True)
    color = models.OneToOneField(Color, on_delete=models.CASCADE)
    size = models.OneToOneField(Size, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.brand_name


class Order(models.Model):
    STATUS = (
        ('pending', 'pending'),
        ('out for delivery', 'out for delivery'),
        ('delivered', 'delivered'),
    )
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.product.name
