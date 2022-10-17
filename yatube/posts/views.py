from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def group(request):
    return HttpResponse('Группы')


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_posts(request, pk):
    return HttpResponse(f'Мороженое номер {pk}')

