from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DefaultConfig(AppConfig):
    name = 'todos.triggers'
    verbose_name = _("ToDo app's triggers")
    label = 'todos_triggers'
