# views.py
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Shoes
from .forms import ShoeForm

class ShoeCreateView(CreateView):
    model = Shoes
    form_class = ShoeForm
    template_name = 'shoe_form.html'  # Создайте этот шаблон
    success_url = reverse_lazy('shoe_list')  # Укажите, куда перенаправить после успешного добавления
