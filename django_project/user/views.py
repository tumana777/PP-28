from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from user.forms import CustomUserCreationForm

class UserRegisterView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('store:home')

    def form_valid(self, form):
        user = form.save()

        login(self.request, user)

        return super().form_valid(form)

class UserLoginView(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('store:home')

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('store:home')