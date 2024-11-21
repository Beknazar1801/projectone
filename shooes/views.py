from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class ShoesView(TemplateView):
    template_name = 'pages/shoes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Добро пожаловать на страницу обуви'
        return context
