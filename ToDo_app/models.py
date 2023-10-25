from django.db import models

# Create your models here.


class ToDoTask(models.Model):
    choices = [(1, 'In Progress'), (2, 'Completed')]

    task = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=choices, default=1)

    class Meta:
        db_table = 'ToDoTask'

    def __str__(self):
        return f'{self.task}'
