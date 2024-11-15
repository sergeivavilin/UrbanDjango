from django.shortcuts import render
from django.views.generic import TemplateView


class MainPage(TemplateView):
    template_name = 'task4/main_page.html'
    extra_context = {
        'title': 'Главная страница магазина',
    }



class ShopPage(TemplateView):
    template_name = 'task4/shop.html'
    extra_context = {
        'title': 'Фигурки из Звездных Войн',
    }



class CartPage(TemplateView):
    template_name = 'task4/cart.html'
    extra_context = {
        'title': 'Ваша корзина',
    }