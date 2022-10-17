from django.urls import path

from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    path('group/', views.group),   
    path('group/<slug:pk>/', views.group_posts)
]
