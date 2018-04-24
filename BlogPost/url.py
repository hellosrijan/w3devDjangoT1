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
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.indexblog, name='index'),
    re_path('^Blog/Details/(?P<id>\d+)/$', views.details, name='details'),
    re_path('^BlogPost/$', views.get_post, name='getpost'),
    re_path('^BlogPost/MyPost/$', views.viewpost, name='viewpost'),
    re_path('^BlogPost/MyPost/EditPost/(?P<pid>\d+)/$', views.editpost, name='editpost'),
    re_path('^BlogPost/MyPost/Delete/(?P<pid>\d+)/$', views.deletepost, name='deletepost')
]
