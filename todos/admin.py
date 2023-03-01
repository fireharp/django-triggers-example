from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_finished', 'user')


admin.site.register(Todo, TodoAdmin)
