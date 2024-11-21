from django.shortcuts import render,redirect
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required


def profile_view(request):
    return render(request, 'pages/profile.html')


class EditProfileView(UpdateView):
    model = User
    fields = ['username', 'email']
    template_name = 'pages/edit_profile.html'
    success_url = reverse_lazy('profile')  # После успешного редактирования будет редирект на страницу профиля
    
    def get_object(self):
        return self.request.user  # Убедитесь, что пользователь редактирует только свой профиль
    



@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'pages/edit_profile.html', {'form': form})
