from datetime import date, timedelta

from django.db.models import Sum, F

from .models import Client, Order, Product, OrderProducts
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import ImageForm
from . import models
from . import forms


def index(request):
    """Главная страница."""
    return render(request, 'index.html')


def about(request):
    """Страница About."""
    return render(request, 'about.html')


def get_all_products(request):
    products = models.Product.objects.all()
    return render(request, 'products.html', {'products': products})


def change_product(request, product_id):
    product = models.Product.objects.filter(pk=product_id).first()
    form = forms.ProductForm(request.POST, request.FILES)
    if request.method == 'POST' and form.is_valid():
        image = form.cleaned_data['image']
        if isinstance(image, bool):
            image = None
        if image is not None:
            fs = FileSystemStorage()
            fs.save(image.name, image)
        product.name = form.cleaned_data['name']
        product.description = form.cleaned_data['description']
        product.price = form.cleaned_data['price']
        product.amount = form.cleaned_data['amount']
        product.image = image
        product.save()
        return redirect('products')
    else:
        form = forms.ProductForm(initial={'name': product.name, 'description': product.description,
                                          'price': product.price, 'amount': product.amount, 'image': product.image})

    return render(request, 'change_product.html', {'form': form})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES) # request.POST чтобы получить текстовую информацию , request.FILES чтобы получить байты
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()  # FileSystemStorage экземпляр позволяет работать с файлами
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})


def clients_list(request):
    """Список клиентов."""
    clients = Client.objects.all()
    context = {'clients': clients}
    return render(request, 'clients_list.html', context)


def client_orders(request, client_id):
    """Отображение заказов пользователя.

    :client_id: код клиента, по которому проводится выборка
    """
    client = get_object_or_404(Client, pk=client_id)
    # orders = Order.objects.prefetch_related('products').select_related('order_prods').filter(client_id=client_id)

    order_prods = OrderProducts.objects.select_related('product').select_related('order').filter(
        order__client_id=client_id).order_by('-order_id')

    order_prods = order_prods.annotate(prod_cost=F('product__price') * F('product_count'))

    context = {
        'client_name': client.client_name,
        'orders': order_prods,
    }

    return render(request, 'client_orders.html', context)


def client_prods(request, client_id, days_history):
    """
    Список товаров заказанных клиентом за определенное кол-во дней.

    :client_id: клиент по которому проводится выборка
    :days_history: кол-во дней, за которые проводится просмотр истории
    """
    client = get_object_or_404(Client, pk=client_id)
    date_start = date.today() - timedelta(days=days_history)

    prod_info = OrderProducts.objects.select_related('product').select_related('odrders').filter(
        order__order_date__gte=date_start, order__client_id=client_id)
    prod_info = prod_info.values('product__prod_name', 'product__price').annotate(count_prod=Sum('product_count'))
    prod_info = prod_info.annotate(cost=F('product__price') * F('count_prod'))

    context = {
        'client_name': client.client_name,
        'period': period(days_history),
        'products': prod_info
    }

    return render(request, 'client_products.html', context)


def period(days: int) -> str:
    """Период отчетности."""
    match days:
        case 7:
            return 'за последнюю неделю'
        case 30:
            return 'за последний месяц'
        case 365:
            return 'за последний год'
    return 'за произвольный период'