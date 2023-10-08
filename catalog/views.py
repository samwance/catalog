from django.shortcuts import render

from catalog.models import Product

def index(request):
    context = {
        'title': 'Главная',
        'products': Product.objects.all()[:5]

    }
    print(context['products'])
    return render(request, 'catalog/index.html', context=context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'You have new message from {name}({email}): {message}')
    return render(request, 'catalog/contact.html')

def product(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'product_detail.html', context)