from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
from . import views

urlpatterns = [
   
    path('login/', LoginView.as_view(template_name='pages/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', register, name='register'),
    path('order-success/', views.order_success, name='order_success'),
]