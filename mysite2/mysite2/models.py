from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ToDoList(models.Model):
    # type of fill that we store from the database
    # every list with belong to a user
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)  # <--- added
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
