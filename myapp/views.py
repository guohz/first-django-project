from django.shortcuts import render
from .models import Task
def index(request):
    task_list = Task.objects.all()
    ctx = {
        'task_list': task_list
    }
    return render(request,'index.html',ctx)
