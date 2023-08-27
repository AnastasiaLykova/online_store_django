from django.shortcuts import render

from catalog.models import Product


def home(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list,
        'title': 'Главная'
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new message from {name}({phone}): {message}')
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)


def product(request, pk):
    context = {
        'object': Product.objects.get(pk=pk),
        'title': 'Продукт'
    }
    return render(request, 'catalog/product.html', context)

