"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from lib2to3.fixes.fix_input import context

from django.contrib import admin
from django.urls import path

from task2.views import index, index2
from task4.views import MainPage, ShopPage, CartPage
from task5.views import sign_up_by_django, sign_up_by_html


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index),
    # path('index2/', index2.as_view()),
    # Shop pages
    # path('main_page/', MainPage.as_view()),
    # path('main_page/shop/', ShopPage.as_view()),
    # path('main_page/cart/', CartPage.as_view()),
    # Registration pages
    path('', sign_up_by_html),
    path('django_sign_up/', sign_up_by_django.as_view()),
]
