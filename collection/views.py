from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class CollectionView(TemplateView):
    template_name = 'pages/collection.html'