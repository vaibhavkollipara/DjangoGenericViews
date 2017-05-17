from django.shortcuts import render
from rest_framework.generics import (ListAPIView,
                                     CreateAPIView,
                                     RetrieveUpdateDestroyAPIView
                                     )
from rest_framework.permissions import AllowAny
from .serializers import TodoItemSerializer, TodoItemListSerializer
from main.models import TodoItem


class TodoList(ListAPIView):
    """
    ApiView to view all todo items list
    """
    serializer_class = TodoItemListSerializer
    permission_class = [AllowAny]

    def get_queryset(self):
        return TodoItem.objects.all()


class CreateTodo(CreateAPIView):
    """
    ApiView to create new todo item
    """
    serializer_class = TodoItemSerializer
    permission_class = [AllowAny]


class ToDoItemView(RetrieveUpdateDestroyAPIView):
    """
    ApiView to view, update and delete todo item
    """
    serializer_class = TodoItemSerializer
    permission_class = [AllowAny]
    lookup_url = 'pk'
    queryset = TodoItem.objects.all()
