"""w3devDjangoT1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path, include
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordChangeDoneView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, LoginView, LogoutView, PasswordChangeView


urlpatterns = [
    path('', views.accounts, name='accounts'),
    path('signin/', LoginView.as_view(template_name='accounts/SignIn.html'), name='SignIn'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('signout/', LogoutView.as_view(template_name='accounts/SignOut.html'), name='SignOut'),
    path('signup/', views.signup, name='SignUp'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('change/password/', PasswordChangeView.as_view(template_name='accounts/ChangePassword.html'), name='change_password'),
    path('change/password/done/', PasswordChangeDoneView.as_view(template_name='accounts/ResetPasswordConfirm.html'), name='password_change_done'),

    path('reset/password/', PasswordResetView.as_view(),
            {'template_name': 'accounts/ResetPassword.html'},
            name='password_reset'),

    path('reset/password/done/$', PasswordResetDoneView.as_view(),
            {'template_name': 'accounts/ResetPasswordSent.html'},
            name='password_reset_done'),
            
    path('reset/rassword/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            PasswordResetConfirmView.as_view(),
            {'template_name': 'accounts/ResetPasswordConfirm.html'},
            name='password_reset_confirm'),

    path('reset/password/complete/', PasswordResetCompleteView.as_view(),
            {'template_name': 'accounts/ResetPasswordComplete.html'},
            name='password_reset_complete'),
]
