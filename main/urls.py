from django.conf.urls import url
from .views import (TodoList,
                    CreateToDo,
                    DeleteToDo,
                    UpdateToDo,
                    ToDoDetail
                    )

app_name = 'main'

urlpatterns = [
    url(r'^$', TodoList.as_view(), name='todolist'),
    url(r'^add$', CreateToDo.as_view(), name='add'),
    url(r'^detail/(?P<pk>[0-9]+)$', ToDoDetail.as_view(), name='detail'),
    url(r'^delete/(?P<pk>[0-9]+)$', DeleteToDo.as_view(), name='delete'),
    url(r'^update/(?P<pk>[0-9]+)$', UpdateToDo.as_view(), name='update')
]
