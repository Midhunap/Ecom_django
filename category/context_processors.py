from category.models import Category


def menu_links(request):  #allcategories #we can access the context processor in all the themplate
    links = Category.objects.all()
    return dict(links = links)  #pass the categories to the navebar.html