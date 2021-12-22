from django.shortcuts import get_object_or_404, render

from category.models import Category
from .models import Product

# Create your views here.
def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None :                                       #store/shirts ,it filter the category by slug
        categories = get_object_or_404(Category, slug=category_slug) #brings the category
        products = Product.objects.filter(category=categories, is_available = True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True) #to view the all product item which is available
        product_count = products.count()
    
    context ={
        'products':products,
        'product_count' : product_count
    }
    return render(request,'store/store.html',context)


# single product details
def product_details(request,category_slug,product_slug):
    try:
        single_product = Product.objects.get(category__slug = category_slug, slug = product_slug) #brings the single product
    except Exception as e:
        raise e
    context = {
        'single_product': single_product
    }    

    return render(request,'store/product_details.html',context)