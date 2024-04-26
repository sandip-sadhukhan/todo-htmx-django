from django.shortcuts import render
from django.http import Http404
from myapp import models

def index(request):
    if request.method == "POST":
        models.Todo.objects.create(text=request.POST.get("text"))
        todos = models.Todo.objects.all().order_by("-created_at")
        return render(request, "todos.html", {"todos": todos})

    todos = models.Todo.objects.all().order_by("-created_at")
    return render(request, "index.html", {"todos": todos})

def deleteTodo(request, todoId):
    if request.method != "DELETE":
        raise Http404
    
    models.Todo.objects.get(id=todoId).delete()

    todos = models.Todo.objects.all().order_by("-created_at")
    return render(request, "todos.html", {"todos": todos})

def editTodo(request, todoId):
    if request.method == "GET":
        todo = models.Todo.objects.get(id=todoId)
        return render(request, "edit-todo.html", {"todo": todo})
    elif request.method == "POST":
        todo = models.Todo.objects.get(id=todoId)
        todo.text = request.POST.get("text")
        todo.save()
        todos = models.Todo.objects.all().order_by("-created_at")
        return render(request, "todos.html", {"todos": todos})

    
