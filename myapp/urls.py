from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.index, name="index"),
    path("deleteTodo/<int:todoId>", views.deleteTodo, name="deleteTodo"),
    path("editTodo/<int:todoId>", views.editTodo, name="editTodo"),
]