from django.conf.urls import url, include
from .views import (TodoList,
                    CreateTodo,
                    ToDoItemView)

app_name = 'api'

urlpatterns = [
    url(r'^todolist$', TodoList.as_view(), name='todolist'),
    url(r'^add$', CreateTodo.as_view(), name='add'),
    url(r'^detail/(?P<pk>[0-9]+)$', ToDoItemView.as_view(), name='detail'),
    url(r'^docs', include('rest_framework_docs.urls')),
]
