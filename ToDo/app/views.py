from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo


def Home(request):
    return render(request, 'home.html')  # Make sure home.html exists in your templates

def to_do(request):
    if request.method == 'POST':
        form = TodoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('todo')  # Redirect to avoid resubmission on refresh
    else:
        form = TodoForm()

    todos = Todo.objects.all().order_by('-id') 
    print(f"Number of todos: {todos.count()}")

    return render(request, 'todo.html', {'form': form, 'todos': todos})
