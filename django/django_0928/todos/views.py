from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos' : todos
    }
    return render(request, 'todos/index.html', context)

def create(request):
    todo = request.GET
    content = todo['content']
    priority = todo['priority']
    deadline = todo['deadline']
    if todo['priority'] == 'select_value' and todo['deadline'] == '':
        Todo.objects.create(content=content)
    elif todo['priority'] == 'select_value':
        Todo.objects.create(content=content, deadline=deadline)
    elif todo['deadline'] == '':
        Todo.objects.create(content=content, priority=priority)
    else:
        Todo.objects.create(content=content, priority=priority, deadline=deadline)
    
    todos = Todo.objects.all()
    context = {
        'todos' : todos
    }
    return redirect('todos:index')

def delete(request, todo_pk):
    d = Todo.objects.get(pk = todo_pk)
    d.delete()
    return redirect('todos:index')

def update(request, todo_pk):
    u = Todo.objects.get(pk = todo_pk)
    if u.completed == False:
        u.completed = True
    else:
        u.completed = False
    u.save()
    return redirect('todos:index')

def detail(request, todo_pk):
    todo = Todo.objects.get(pk = todo_pk)
    context = {
        'todo' : todo
    }
    return render(request, 'todos/detail.html', context)

def edit(request, todo_pk):
    todo = Todo.objects.get(pk = todo_pk)
    context = {'todo': todo}
    return render(request, 'todos/edit.html', context)

def upload(request, todo_pk):
    todo = Todo.objects.get(pk = todo_pk)
    content = request.GET.get('content')
    todo.content = content
    todo.save()
    return redirect('todos:detail', todo_pk)