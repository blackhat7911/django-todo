from django.contrib import admin
from django.urls import path
from . import views
#from rest_framework import routers

#router = routers.DefaultRouter()
#router.register(r'todos', views.TodoView, 'todo')

urlpatterns = [
    path('', views.index, name="index"),
    path('api/', views.TodoView, name="api"),
]

