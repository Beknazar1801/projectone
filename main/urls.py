from django.contrib import admin
from django.urls import path
from .views import *
from .qwerty import ShoeCreateView
from . import views




urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('collection/', CollectionBaseView.as_view(), name='collection'),
    path('shoe/<int:pk>/', ShoeDetailView.as_view(), name='shoe_detail'),
    path('shoe/add/', ShoeCreateView.as_view(), name='shoe_add'),
    path('random-shoes/', RandomShoesListView.as_view(), name='random_shoes'),
    path('shoes/', ShoeListView.as_view(), name='shoe_list'), # глушиться потому что этот юрлка работает 
    path('shoe/<int:shoe_id>/review/', views.leave_review, name='leave_review'),
    path('delivery-info/', views.delivery_info, name='delivery_info'),
    ]


