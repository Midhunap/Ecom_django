from enum import unique
from django.db import models
from django.urls.base import reverse

from category.models import Category

# Create your models here.
class Product(models.Model):
    product_name  = models.CharField(max_length=200 , unique=True)
    slug = models.SlugField(max_length=200 , unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    stock =models.IntegerField()
    image = models.ImageField(upload_to ='photos/products')
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE) #forienkey ,category is inherited here 
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url_slug(self):
        return reverse('product_details',args=[self.category.slug,self.slug])

    def __str__(self):
        return self.product_name
        