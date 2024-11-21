from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import TemplateView,ListView, DetailView
from .models import *
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Shoes, Rating, Review
from .forms import RatingForm, ReviewForm
from django.db.models import Avg
from django.contrib import messages
from django.views import View







# Create your views here.


# class MainView(TemplateView):
#     model = Shoes
#     template_name = 'pages/home.html'
#     context_object_name = 'shoes'

class MainView(ListView):
    model = Shoes
    template_name = 'pages/home1.html'
    context_object_name = 'shoes'


# class TestView(TemplateView):
#     template_name = 'pages/test.html'


class CollectionBaseView(ListView):
    model = Shoes
    template_name = 'pages/collection.html'  # Укажите ваш файл шаблона
    context_object_name = 'shoes_lists'  # Укажите имя переменной для доступа в шаблоне
    queryset = Shoes.objects.all()    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shoes'] = Shoes.objects.all()  # Получаем все объекты обуви
        return context



class ShoeDetailView(DetailView):
    model = Shoes
    template_name = 'pages/shoe_detail.html'
    context_object_name = 'shoe'



class RandomShoesListView(ListView):
    model = Shoes
    template_name = 'pages/shoes.html'  # Ваш шаблон для отображения обуви
    context_object_name = 'shoes_list'

    def get_queryset(self):
        # Возвращаем случайный набор объектов
        return Shoes.objects.order_by('?')[:10]
    



class ShoeListView(ListView):
   model = Shoes
   template_name = 'pages/shoe_list.html'
   context_object_name = 'shoes'

   def get_queryset(self):
       queryset = super().get_queryset()
       
       # Фильтрация по категории пола (если есть)
       category = self.request.GET.get('category')
       if category:
           queryset = queryset.filter(gender_category__name=category)
       
       # Фильтрация по бренду (если выбран бренд)
       brand_id = self.request.GET.get('brand')
       if brand_id:
           queryset = queryset.filter(brend_id=brand_id)
       
       return queryset

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['brands'] = Brends.objects.all()
       return context


def home(request):
    # Получаем категории мужской и женской обуви
    male_category = GenderCategory.objects.get(name='M')
    female_category = GenderCategory.objects.get(name='F')
    
    # Ограничиваем вывод 3 товарами для каждой категории
    men_shoes = Shoes.objects.filter(gender_category=male_category)[:3]
    women_shoes = Shoes.objects.filter(gender_category=female_category)[:3]

    # Получаем все доступные бренды
    brands = Brends.objects.all()

    return render(request, 'home.html', {
        'men_shoes': men_shoes,
        'women_shoes': women_shoes,
        'brands': brands,  # Добавляем бренды в контекст
    })

@login_required
def add_rating(request, shoe_id):
    shoe = get_object_or_404(Shoes, id=shoe_id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.shoe = shoe
            rating.user = request.user
            rating.save()
            return redirect('shoe_detail', shoe_id=shoe.id)
    else:
        form = RatingForm()
    return render(request, 'main/add_rating.html', {'form': form, 'shoe': shoe})

@login_required
def add_review(request, shoe_id):
    shoe = get_object_or_404(Shoes, id=shoe_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.shoe = shoe
            review.user = request.user
            review.save()
            return redirect('shoe_detail', shoe_id=shoe.id)
    else:
        form = ReviewForm()
    return render(request, 'main/add_review.html', {'form': form, 'shoe': shoe})

def shoe_detail(request, pk):
    shoe = Shoes.objects.get(pk=pk)
    reviews = Review.objects.filter(shoe=shoe)

    # Добавляем в контекст заполненные и пустые звезды для каждого отзыва
    for review in reviews:
        review.stars_filled = range(review.rating)  # Заполненные звезды
        review.stars_empty = range(5 - review.rating)  # Пустые звезды

    return render(request, 'shoe_detail.html', {'shoe': shoe, 'reviews': reviews})

#def shoe_detail(request, pk):
#    shoe = get_object_or_404(Shoes, pk=pk)
#    reviews = shoe.review_set.all()
#    average_rating = reviews.aggregate(Avg('rating'))['rating__avg'] if reviews.exists() else 0
#
#    if request.method == 'POST' and request.user.is_authenticated:
#        # Обработка формы отзыва
#        form = ReviewForm(request.POST)
#        
#        if form.is_valid():
#            # Если форма валидна, сохраняем отзыв
#            Review.objects.create(
#                shoe=shoe,
#                user=request.user,
#                text=form.cleaned_data['text'],
#                rating=form.cleaned_data['rating'] if form.cleaned_data['rating'] else None
#            )
#            # Перенаправляем на страницу с деталями обуви
#            return redirect('shoe_detail', pk=shoe.id)
#    else:
#        form = ReviewForm()  # Пустая форма для GET запроса
#
#    return render(request, 'pages/shoe_detail.html', {
#        'shoe': shoe,
#        'reviews': reviews,
#        'average_rating': average_rating,
#        'form': form,  # передаем форму в шаблон
#    })



@login_required
def leave_review(request, shoe_id):
    shoe = get_object_or_404(Shoes, pk=shoe_id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        
        if form.is_valid():
            # Если форма валидна, создаём новый отзыв
            Review.objects.create(
                shoe=shoe,
                user=request.user,
                text=form.cleaned_data['text'],
                rating=form.cleaned_data['rating'] if form.cleaned_data['rating'] else None
            )
            
            # Перенаправляем на страницу с деталями обуви
            return redirect('shoe_detail', pk=shoe_id)
    else:
        form = ReviewForm()  # Пустая форма для GET запроса

    # Получаем список отзывов и средний рейтинг
    reviews = shoe.review_set.all()
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg'] if reviews.exists() else 0

    return render(request, 'pages/shoe_detail.html', {
        'shoe': shoe,
        'reviews': reviews,
        'average_rating': average_rating,
        'form': form,
    })
    

def home(request):
    # Извлекаем все обуви и сортируем их случайным образом
    shoes = Shoes.objects.all().order_by('?')
    
    return render(request, 'pages/home.html', {'shoes': shoes})
    
def delivery_info(request):
    return render(request, 'pages/delivery_info.html')
    


    







