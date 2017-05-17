from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
from main.models import TodoItem


class TodoItemSerializer(ModelSerializer):

    class Meta:
        model = TodoItem
        fields = ['title', 'description', 'date_created']


class TodoItemListSerializer(ModelSerializer):

    class Meta:
        model = TodoItem
        fields = ['title', 'description', 'url', 'date_created']

    url = HyperlinkedIdentityField(
        view_name='api:detail',
        lookup_field='pk'
    )
