from django.urls import path
from . import views

from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.login_view, name = 'login'),
    path('register', views.register, name='register'),
    path('logout', views.logout_view, name = 'logout'),
    path('home', views.home, name='home'),

    # password rest urlpatterrns
    path('reset_password',
    auth_views.PasswordResetView.as_view(template_name="loginApp/password_reset.html"),
    name='reset_password'),

    path('reset_password_sent',
    auth_views.PasswordResetDoneView.as_view(template_name="loginApp/reset_password_sent.html"),
    name='password_reset_done'),

    path('reset/<uidb64>/<token>',
    auth_views.PasswordResetConfirmView.as_view(template_name="loginApp/set_password.html"),
    name = 'password_reset_confirm'),

    path('reset_password_complete',
    auth_views.PasswordResetCompleteView.as_view(template_name="loginApp/reset_password_done.html"),
    name = 'password_reset_complete'),
]
