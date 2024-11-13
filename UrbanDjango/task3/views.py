from django.shortcuts import render
from django.views.generic import TemplateView


class MainPage(TemplateView):
    template_name = 'task3/main_page.html'


class ShopPage(TemplateView):
    template_name = 'task3/shop.html'


class CartPage(TemplateView):
    template_name = 'task3/cart.html'