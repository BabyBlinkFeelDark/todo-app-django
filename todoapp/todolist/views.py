
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .models import ToDo


# Create your views here.

def index(request):
    todos = ToDo.objects.all()
    return render(request, 'todoapp/index.html', {"todo_list":todos, "title":"Main"},)

@require_http_methods(['POST'])
def add(request):
    title = request.POST['title']
    todo = ToDo(title = title)
    todo.save()
    return redirect('index')

def update(request, todo_id):
    todo = ToDo.objects.get(id = todo_id)
    todo.is_complite = not todo.is_complite
    todo.save()
    return redirect('index')

def delete(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')
