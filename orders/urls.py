from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('order/<int:shoe_id>/', views.create_order, name='create_order'),
    path('order_success/', views.order_success, name='order_success'),
]
