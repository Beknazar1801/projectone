from django.contrib import admin
from .models import Category, Brends, Size, Shoes, GenderCategory
from .models import Review 

# Регистрация модели Category с использованием декоратора
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'image']

# Регистрация модели Brends
class BrendsAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    search_fields = ('name',)
    list_filter = ('name',)

admin.site.register(Brends, BrendsAdmin)

# Регистрация модели Size
class SizeAdmin(admin.ModelAdmin):
    list_display = ('size',)
    search_fields = ('size',)

admin.site.register(Size, SizeAdmin)

# Регистрация модели Shoes
class ShoesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'brend', 'gender_category')  # Поля, которые будут отображаться
    list_filter = ('gender_category', 'category', 'brend')  # Фильтры по полям
    search_fields = ('name', 'description')  # Возможность поиска по названию и описанию
    list_editable = ('gender_category',)  # Поле gender_category будет редактируемым в списке

admin.site.register(Shoes, ShoesAdmin)

# Регистрация модели GenderCategory с использованием декоратора
@admin.register(GenderCategory)
class GenderCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('shoe', 'user', 'rating', 'created_at')  # Поля для отображения в списке
    search_fields = ('shoe__name', 'user__username', 'text')  # Поиск по обуви, пользователю и тексту отзыва
    list_filter = ('rating', 'created_at')  # Фильтрация по рейтингу и дате создания
    ordering = ('-created_at',)  # Сортировка по дате (от новых к старым)
    readonly_fields = ('created_at',)  # Сделать поле даты создания только для чтения

# Регистрируем модель в админке
admin.site.register(Review, ReviewAdmin)