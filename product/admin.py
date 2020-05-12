from django.contrib import admin

# Register your models here.
from .models import Product, Order, Tag, Color, Size
admin.site.register(Color)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Tag)
admin.site.register(Size)

