# forms.py
from django import forms
from .models import Shoes
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Rating, Review

class ShoeForm(forms.ModelForm):
    class Meta:
        model = Shoes
        fields = ['name', 'description', 'price', 'image']  # Укажите поля, которые вы хотите включить




class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),}  # Рейтинг от 1 до 5




