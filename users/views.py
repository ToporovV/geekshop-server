from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from users.forms import UserLoginForm, UsersRegisterForm, UserProfileForm
from users.models import User
from baskets.models import Basket


class UserLoginView(LoginView):
    model = User
    template_name = 'users/login.html'
    form_class = UserLoginForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserLoginView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Авторизация'
        return context


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = UsersRegisterForm
    success_url = reverse_lazy('users:login')
    success_message = 'Вы успешно зарегистрировались!'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Регистрация'
        return context


class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')
    success_message = 'Изменения успешно сохранены!'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Личный кабинет'
        context['baskets'] = Basket.objects.filter(user=self.request.user)
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.request.user.id)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)


class UserLogoutView(LogoutView):
    model = User
    template_name = 'products/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserLogoutView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop'
        return context
