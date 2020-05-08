from django.db import models
from django.utils.timezone import now

# Create your models here.

class Add_product(models.Model):
    name = models.CharField(max_length=30,null=True,blank=True)
    sub_name = models.CharField(max_length=30,null=True,blank=True)
    p_image = models.ImageField(upload_to='products',blank=True,null=True)
    size = models.CharField(max_length=10,null=True,blank=True)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)


    

  

   