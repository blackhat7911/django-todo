from django.shortcuts import render
from django.http import HttpResponse
from .serializers import TodoSerializer
from .models import Todo
from rest_framework import viewsets

# Create your views here.

def index(request):
    todo = Todo.objects.all()
    context = {
        'todo': todo,
    }
    return render(request, "index.html", context)

# viewsets provides implementation for CRUD operations
class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()