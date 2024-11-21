from django.shortcuts import render, get_object_or_404, redirect
from main.models import Shoes
from .models import Order

from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Shoes, Order
from .form import OrderForm # Предположим, что вы используете форму для заказа
from django.http import HttpResponse
from main.models import *

from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from .form import OrderForm
from main.models import Shoes

def create_order(request, shoe_id):
    shoe = Shoes.objects.get(id=shoe_id)  # Получаем обувь по ID

    if request.method == 'POST':
        # Создаем заказ без учета размера
        order = Order.objects.create(
            shoe=shoe,
            quantity=request.POST.get('quantity'),
            delivery_address=request.POST.get('address')
        )
        return redirect('order_success')  # Перенаправление на страницу успешного заказа

    return render(request, 'order/create_order.html', {'shoe': shoe})

 


def order_success(request):
    return render(request, 'pages/order_success.html')


