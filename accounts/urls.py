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
from django.contrib.auth.views import (
    login,
    logout,
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete
    )
urlpatterns = [
    path('', views.accounts, name='accounts'),
    re_path(r'^SignIn/$', login, {'template_name': 'accounts/SignIn.html'}, name='SignIn'),
    re_path(r'^auth/', include('social_django.urls', namespace='social')),
    re_path(r'^SignOut/$', logout, {'template_name': 'accounts/SignOut.html'}, name='SignOut'),
    re_path(r'^SignUp/$', views.signup, name='SignUp'),
    re_path(r'^Profile/$', views.view_profile, name='view_profile'),
    re_path(r'^Profile/Edit/$', views.edit_profile, name='edit_profile'),
    re_path(r'^ChangePassword/$', views.change_password, name='change_password'),
    re_path(r'^ResetPassword/$', password_reset,
            {'template_name': 'accounts/ResetPassword.html'},
            name='password_reset'),
    re_path(r'^ResetPassword/Done/$', password_reset_done,
            {'template_name': 'accounts/ResetPasswordSent.html'},
            name='password_reset_done'),
    re_path(r'^ResetPassword/Confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            password_reset_confirm,
            {'template_name': 'accounts/ResetPasswordConfirm.html'},
            name='password_reset_confirm'),
    re_path(r'^ResetPassword/Complete/$', password_reset_complete,
            {'template_name': 'accounts/ResetPasswordComplete.html'},
            name='password_reset_complete'),
]
