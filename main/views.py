from django.shortcuts import render
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from .models import TodoItem


class TodoList(generic.ListView):
    template_name = 'main/list.html'
    context_object_name = 'items'

    def get_queryset(self):
        return TodoItem.objects.all()


class ToDoDetail(generic.DetailView):
    template_name = 'main/item.html'
    model = TodoItem


class CreateToDo(generic.CreateView):
    model = TodoItem
    fields = ['title', 'description']


class UpdateToDo(generic.UpdateView):
    model = TodoItem
    fields = ['title', 'description']


class DeleteToDo(generic.DeleteView):
    model = TodoItem
    success_url = reverse_lazy('main:todolist')
