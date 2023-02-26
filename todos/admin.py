from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('date_completed', 'title', 'user')


admin.site.register(Todo, TodoAdmin)
