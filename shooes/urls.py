from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('shoes/', ShoesView.as_view(), name='shoes'),
]