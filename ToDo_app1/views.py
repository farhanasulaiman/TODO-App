from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils import timezone
from pip._internal import req

from ToDo_app1.forms import ToDoForm
from ToDo_app1.models import Todo


# Create your views here.
def f_index(request):
    return render(request, "index.html")


def f_admindex(request):
    return render(request, "admin_temp/index.html")


# create form
def create(request):
    form = ToDoForm()
    if request.method == "POST":
        form1 = ToDoForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('view')
        else:
            form = form1
            # messages.info(request,"Due date cannot be in the past.")
    else:
        initial_data = {'date': timezone.now().date()}
        form = ToDoForm(initial=initial_data)
    return render(request, "add.html", {"form": form})


def view(request):
    data = Todo.objects.all()
    return render(request, "view.html", {"data": data})


def delete(request, id):
    if request.method == "POST":
        del1 = Todo.objects.get(id=id)
        del1.delete()
        return redirect("view")  # url_name(given in urls.py) to which it is to be redirected
    return render(request, "view.html")


def update_task(request, id):
    record = Todo.objects.get(id=id)
    form = ToDoForm(instance=record)
    if request.method == 'POST':
        form1 = ToDoForm(request.POST, instance=record)
        if form1.is_valid():
            form1.save()
            return redirect("view")
        else:
            form = form1
    return render(request, "update.html", {"form": form})
