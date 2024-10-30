from django.shortcuts import render
from django.shortcuts import redirect
from .models import Task
# Create your views here.


def home(request):
    tasks = Task.objects.all()
    return render(request, 'todoapp/home.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        task_title = request.POST.get('task')
        task_status = request.POST.get('status', 'NS')  # Default to 'NS' if not specified
        if task_title:
            Task.objects.create(title=task_title, status=task_status)
    return redirect('home-page')


def complete_task(request, id):
    task = Task.objects.get(id=id)
    task.completed = True
    task.save()
    return redirect('home-page')

from django.shortcuts import get_object_or_404, redirect, render
from .models import Task


def update_status(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        new_status = request.POST.get('status')
        if new_status in dict(Task.STATUS_CHOICES):
            task.status = new_status
            task.save()
    return redirect('home-page')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('home-page')
