from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Tasks

# Create your views here.
def index(request):
    # Create a object holding all tasks
    mytasks = Tasks.objects.all().values()

    # Load index.html as the template for this view
    template = loader.get_template('index.html')
    context = {
        'mytasks' : mytasks,
    }
    return HttpResponse(template.render(context, request))


def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addtask(request):
    # Grab information from the form
    name = request.POST['name']
    description = request.POST['description']

    # Create a new temp task and save it
    task = Tasks(task_name = name, task_description = description)
    task.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    # Locate the entry using id
    task = Tasks.objects.get(id=id)
    task.delete()
    return HttpResponseRedirect(reverse('index'))

def edit(request, id):
    mytask = Tasks.objects.get(id=id)
    template = loader.get_template('edit.html')
    context = {
        'mytask': mytask,
    }
    return HttpResponse(template.render(context, request))

def edittask(request, id):
    # Grab information from the form
    name = request.POST['name']
    description = request.POST['description']

    # Locate the entry using id and update the results
    task = Tasks.objects.get(id=id)
    task.task_name = name
    task.task_description = description
    task.save()

    return HttpResponseRedirect(reverse('index'))