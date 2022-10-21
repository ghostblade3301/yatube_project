from .models import Post, Group
from django.shortcuts import render, get_object_or_404


def index(request):
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'title': title,
        'posts': posts
    }
    return render(request, template, context)


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_posts(request, slug):
    # Функция get_object_or_404 получает по заданным критериям объект
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('group')[:10]
    template = 'posts/group_list.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'group': group,
        'posts': posts,
        'title': title,
    }
    return render(request, template, context)
