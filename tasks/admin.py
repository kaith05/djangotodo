from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'status', 'due_date', 'created_at')
    list_filter = ('status', 'due_date', 'user')
    search_fields = ('title', 'description')
