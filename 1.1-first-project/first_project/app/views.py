import os
import datetime

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'

    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    time = datetime.datetime.now()
    time_string = time.strftime("%H:%M:%S")
    msg = f'Текущее время: {time_string}'
    return HttpResponse(msg)


def workdir_view(request):
    files = os.listdir()
    msg = f'Список файлов в рабочей директории: {files}'
    return HttpResponse(msg)
    # raise NotImplemented
