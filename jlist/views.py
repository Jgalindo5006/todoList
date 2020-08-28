from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Todo


# Create your views here.

def home(request):
    todo_items = Todo.objects.all().order_by('-current_date')
    context = {
        'todo_list': todo_items
    }
    return render(request, 'index.html', context)


def add_todo(request):
    current_date = timezone.now()
    content = request.POST['content']
    Todo.objects.create(current_date=current_date, text_list=content)

    return HttpResponseRedirect('/')


def delete_todo(request, todo_id):
    print(todo_id)
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')
