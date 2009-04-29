from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=32)

class Pile(models.Model):
    task = models.ForeignKey(Task)
    comment = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)
