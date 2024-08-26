from django.contrib import admin
from .models import Task
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'isDone', 'date')
    list_filter = ('isDone', 'date')
    search_fields = ('title', 'description')
# Register your models here.
