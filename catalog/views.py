from django.shortcuts import render
from catalog.models import Product


# Create your views here.


def home(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Главная'
    }
    if request.method == 'GET':
        return render(request, 'catalog/home.html', context)


def contacts(request):
    context = {
        'title': 'Контакты'
    }
    if request.method == 'GET':
        return render(request, 'catalog/contacts.html', context)


def product(request, id):
    product_id = Product.objects.get(pk=id)
    context = {
        "name": product_id.name,
        "description": product_id.description,
        "image": product_id.image,
        "category": product_id.category,
        "price": product_id.price,
        "creation_date": product_id.creation_date,
        "last_modified_date": product_id.last_modified_date,
        "title": f"Товар {product_id.name}"
    }
    if request.method == 'GET':
        return render(request=request, template_name='catalog/product.html', context=context)
