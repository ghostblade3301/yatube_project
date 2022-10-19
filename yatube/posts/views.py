#from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = 'posts/index.html'
    text = 'Это главная страница проекта Yatube'
    context = {
        'text': text,
    }
    return render(request, template, context)


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_posts(request):
    template = 'posts/group_posts.html'
    text = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'text': text,
    }
    return render(request, template, context)
