from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import redirect

from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, UpdateView, TemplateView

from Home_Work_Django_2 import settings
from users.forms import CustomAuthenticationForm, UserForm, UserProfileForm
from users.generate_password import password_generator, code_generator
from users.models import User


class LoginView(BaseLoginView):
    template_name = 'users/login.html'
    form_class = CustomAuthenticationForm


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        generated_code = code_generator(6)
        user = form.save()
        user.is_active = False
        user.verification_code = generated_code
        user.save()

        verification_code = str(generated_code) + str(user.pk)
        activation_url = self.request.build_absolute_uri(
            reverse_lazy('users:verify_email', kwargs={
                'verification_code': verification_code
            }
                         )
        )
        send_mail(
            subject='Подтверждение адреса почты',
            message=f'Пожалуйста, '
                    f'перейдите по следующей ссылке, '
                    f'чтобы подтвердить свой адрес электронной почты: '
                    f'{activation_url}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return redirect('users:verification_link_sent')


class SuggestRegister(TemplateView):
    template_name = 'users/suggest_registration.html'
    extra_context = {'title': 'Доступ закрыт'}


class UserConfirmEmailView(View):

    def get(self, request, verification_code):
        uid = int(verification_code[6:])
        code = verification_code[:6]
        try:
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and code == user.verification_code:
            user.is_active = True
            user.verification_code = ""
            user.save()
            return redirect(reverse_lazy('users:email_verified'))
        else:
            return redirect(reverse_lazy('users:verification_failed'))


class EmailConfirmationSentView(TemplateView):
    template_name = 'users/verification_link_sent.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Подтверждение почты'
        return context


class EmailConfirmedView(TemplateView):
    template_name = 'users/email_verified.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Подтверждение почты'
        return context


class EmailConfirmationFailedView(TemplateView):
    template_name = 'users/verification_failed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Подтверждение почты'
        return context


class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    extra_context = {'title': 'Профиль'}
    form_class = UserProfileForm

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = password_generator(size=12)
    send_mail(
        subject='Смена пароля',
        message=f'Вы сгенерировали новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    if request.user.is_authenticated:
        request.user.set_password(new_password)
        request.user.save()
        return redirect(reverse('catalog:home'))
