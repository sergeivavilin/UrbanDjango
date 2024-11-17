from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

from .forms import UserRegister


users = ['admin','user',]

# Реализация через класс и форму
class sign_up_by_django(View):

    def get(self, request: HttpRequest):
        info = {}
        info['form'] = UserRegister()
        return render(request, 'task5/registration_page.html', context=info)

    def post(self, request: HttpRequest):
        info = {}
        form = UserRegister(request.POST)
        info['form'] = form
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']

            # Проверяем наличие пользователя
            if username in users:
                info['error'] = 'Пользователь с таким именем уже существует'
                return render(request, 'task5/registration_page.html', context=info)

            # Проверяем совпадение паролей
            if password != password2:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'task5/registration_page.html', context=info)

            users.append(username)
            info['message'] = f'Приветствуем, {username}!'
        else:
            info['error'] = 'Ошибка в валидации формы'
        return render(request, 'task5/registration_page.html', context=info)

# Реализация через функцию и форму
# def sign_up_by_django(request: HttpRequest):
#     info = {}
#     if request.method == 'POST':
#         form = UserRegister(request.POST)
#         info['form'] = form
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             password2 = form.cleaned_data['password2']
#
#             # Проверяем наличие пользователя
#             if username in users:
#                 info['error'] = 'Пользователь с таким именем уже существует'
#                 return render(request, 'task5/registration_page.html', context=info)
#
#             # Проверяем совпадение паролей
#             if password != password2:
#                 info['error'] = 'Пароли не совпадают'
#                 return render(request, 'task5/registration_page.html', context=info)
#
#             users.append(username)
#             return HttpResponse(f"Приветствуем, {username}!")
#
#     else:
#         form = UserRegister()
#         info['form'] = form
#     return render(request, 'task5/registration_page.html', context=info)


# Реализация через функцию без использования формы
def sign_up_by_html(request: HttpRequest):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')

        # Проверяем наличие пользователя
        if username in users:
            info['error'] = 'Такой пользователь уже есть'
            return render(request, 'task5/registration_page.html', context=info)

        # Проверяем совпадение паролей
        if password != password2:
            info['error'] = 'Пароли не совпадают'
            return render(request, 'task5/registration_page.html', context=info)

        users.append(username)
        info['message'] = f'Приветствуем, {username}!'
    return render(request, 'task5/registration_page.html', context=info)
