from django.contrib import admin
# Register your models here.
from .models import Product, Order, Tag, Color, Size, Subtag
admin.site.register(Color)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Tag)
admin.site.register(Size)
admin.site.register(Subtag)

