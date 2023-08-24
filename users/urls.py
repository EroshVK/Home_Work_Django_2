from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, SuggestRegister, RegisterView, UserUpdateView, generate_new_password
from users.views import EmailConfirmationSentView, UserConfirmEmailView, EmailConfirmedView, EmailConfirmationFailedView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('suggest_register', SuggestRegister.as_view(), name='suggest_register'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('profile/generate_password/', generate_new_password, name='generate_password'),
    path('profile/verify_email/<str:verification_code>/', UserConfirmEmailView.as_view(), name='verify_email'),
    path('profile/verification_link_sent/', EmailConfirmationSentView.as_view(), name='verification_link_sent'),
    path('profile/email_verified/', EmailConfirmedView.as_view(), name='email_verified'),
    path('profile/verification_failed/', EmailConfirmationFailedView.as_view(), name='verification_failed'),
]