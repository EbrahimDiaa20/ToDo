from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm

def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_todos')
    else:
        form = TodoForm()
    return render(request, 'add_todo.html', {'form': form})

def view_todos(request):
    todos = Todo.objects.all()
    return render(request, 'view_todos.html', {'todos': todos})

def edit_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, request.FILES, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('view_todos')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'edit_todo.html', {'form': form, 'todo': todo})

def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'POST':
        todo.delete()
        return redirect('view_todos')
    return render(request, 'confirm_delete.html', {'todo': todo})
