from django.db import models
from main.models import Shoes
  # Импортируйте вашу модель обуви

class Order(models.Model):
    # Вы можете добавить поле пользователя, если хотите, чтобы заказы были связаны с конкретными пользователями

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Пользователь', null=True, blank=True)
    shoe = models.ForeignKey('main.Shoes', on_delete=models.CASCADE, null=True, blank=True)  # Обратите внимание на строку 'main.Shoe'  # Убедитесь, что это поле определено
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=1)
    order_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')
    delivery_address = models.CharField(max_length=255, verbose_name='Адрес доставки')
    

    def __str__(self):
        return f'Order {self.id} by {self.user}'

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ['-order_date']

