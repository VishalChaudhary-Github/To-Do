from django.shortcuts import render
from django.http import HttpResponseRedirect
from ToDo_app.models import ToDoTask
from django.urls import reverse
# Create your views here.


def home(request):
    context = {'task_list': ToDoTask.objects.all().order_by('-created_on', 'status'),
               'total': ToDoTask.objects.all().count(),
               'active': ToDoTask.objects.filter(status=1).count(),
               'completed': ToDoTask.objects.filter(status=2).count()}
    return render(request, 'home.html', context=context)


def add_task(request):
    val = request.POST['TASK']
    ToDoTask.objects.create(task=val)
    url = reverse('todo-home')
    return HttpResponseRedirect(redirect_to=url)


def del_task(request, task_id):
    ToDoTask.objects.get(id=task_id).delete()
    url = reverse('todo-home')
    return HttpResponseRedirect(redirect_to=url)


def task_done(request, task_id):
    ToDoTask.objects.filter(id=task_id).update(status=2)
    url = reverse('todo-home')
    return HttpResponseRedirect(redirect_to=url)