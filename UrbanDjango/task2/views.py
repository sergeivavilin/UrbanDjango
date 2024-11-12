from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    return render(request, 'task2/func_template.html')

class index2(TemplateView):
    template_name = 'task2/class_template.html'