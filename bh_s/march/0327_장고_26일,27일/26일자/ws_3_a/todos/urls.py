from django.urls import path
from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.index, name ='index'),  # todos: index
    path('create_todo/', views.create_todo, name='create'),
    path('<work>/', views.detail, name='detail'),
]



    