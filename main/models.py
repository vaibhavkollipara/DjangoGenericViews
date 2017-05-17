from django.db import models
from django.core.urlresolvers import reverse


class TodoItem(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} : {}".format(self.title, self.description)

    def get_absolute_url(self):
        return reverse('main:detail', kwargs={'pk': self.pk})
