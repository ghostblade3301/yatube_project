from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index, name='main'),
    path('group_posts/', views.group_posts, name='group_posts'),
    path('group/<slug:pk>/', views.group_posts, name='group_posts')
]
