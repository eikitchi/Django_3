from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import ProfileUpdateView, UserRegisterView, EmailConfirmationSentView, UserConfirmEmailView, \
    EmailConfirmedView, EmailConfirmationFailedView, generate_new_password, backup_pass

app_name = UsersConfig.name

urlpatterns = [

    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('email-confirmation-sent/', EmailConfirmationSentView.as_view(), name='email_confirmation_sent'),
    path('confirm-email/<str:uidb64>/<str:token>/', UserConfirmEmailView.as_view(), name='confirm_email'),
    path('email-confirmed/', EmailConfirmedView.as_view(), name='email_confirmed'),
    path('confirm-email-failed/', EmailConfirmationFailedView.as_view(), name='email_confirmation_failed'),
    path('generate_new_password/', generate_new_password, name='generate_new_password'),
    path('backup_pass/', backup_pass, name='backup_pass'),]
    # path('activate/<str:token>/', activate_user, name='activate'),
    # path('page_after_registration/<str:token>/', page_after_registration, name='page_after_registration'),
    # path('backup_pass/', PasswordChangeView_.as_view(), name='backup_pass'),
