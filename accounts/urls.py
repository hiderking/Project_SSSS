from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('AdminForgotpassword/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'),name='AdminForgotpassword'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
    

   
]
