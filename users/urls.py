from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, VerificationView, expectation, UserUpdateView, \
    generate_new_password, PasswordRecoveryView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('register', RegisterView.as_view(), name='register'),
    path('verification/<int:pk>', VerificationView.as_view(), name='verification'),
    path('expectation', expectation, name='expectation'),
    path('profile', UserUpdateView.as_view(), name='profile'),
    path('profile/genpassword', generate_new_password, name='genpassword'),
    path('password_recovery/', PasswordRecoveryView.as_view(), name='password_recovery'),
]
