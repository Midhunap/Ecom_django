from django.db import models
from django.urls import reverse


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255 , blank=True)
    cat_image = models.ImageField(upload_to='photos/categories',blank=True)

    class Meta:
        verbose_name = 'category' #to change the category's' to categor'ies'
        verbose_name_plural = 'categories'

    def get_url_slug(self):
        return reverse('product_by_category',args=[self.slug] ) #All category in store 

    def __str__(self):
        return self.category_name