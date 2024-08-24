from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import TodoForm

def to_do(request):
    if request.method == 'POST':
        form = TodoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Saved")
    else:
        form = TodoForm()
    
    return render(request, 'todo.html', {'form': form})
