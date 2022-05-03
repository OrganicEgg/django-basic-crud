from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.urls import reverse
from .models import Task
import random

app_name="tm"

def index(request):
    task = Task.objects.order_by('pk')
    return render(request, 'taskmanagement/index.html', {
        'tasks': task
    })

def create(request):
    if request.method == "POST":
        task = Task()
        task.name = request.POST['name']
        task.description = request.POST['description']
        task.status = request.POST.get('status', 0)
        task.assigned_to_user_id = 1
        task.created_by_user_id = 1
        task.date_created = timezone.now()
        task.save()
    return render(request, 'taskmanagement/create.html')

def edit(request, pk_id):
    task = get_object_or_404(Task, pk=pk_id)

    if request.method == "POST":
        task.name = request.POST['name']
        task.description = request.POST['description']
        task.status = request.POST.get('status', 0)
        task.last_updated_by_user_id = 1
        task.last_updated_date = timezone.now()
        task.save()

    return render(request, 'taskmanagement/update.html', { 
        'task': task 
    })

def delete(request, pk_id):
    if request.method == "POST":
        task = get_object_or_404(Task, pk=pk_id)
        task.delete()
    return redirect("index")