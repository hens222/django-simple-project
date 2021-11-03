from django.contrib import admin
from .models import ToDoList, Item

# Register your models here.
admin.site.register(ToDoList)  # -> we could see the database on the admin dashboard
admin.site.register(Item)
