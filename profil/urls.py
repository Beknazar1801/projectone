from django.urls import path
from .views import profile_view,edit_profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    
]
