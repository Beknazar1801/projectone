from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'shoe', 'quantity', 'order_date')
    search_fields = ('user__username', 'product__name')

admin.site.register(Order, OrderAdmin)

