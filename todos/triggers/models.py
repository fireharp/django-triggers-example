from triggers.models import Action, Event, Condition
from django.utils.translation import gettext_lazy as _


class TodoIsCompletedEvent(Event):

    class Meta(Event.Meta):
        verbose_name = _('todo is completed event')

    def __str__(self):
        return f'{super().__str__()}'


class CreateTodoAction(Action):
    class Meta(Action.Meta):
        verbose_name = _('create todo action')

    def __str__(self):
        return f'{super().__str__()}'

    def perform(self, user, context):
        # TODO: implement
        pass


class TodoIsImportantCondition(Condition):
    class Meta(Condition.Meta):
        verbose_name = _('todo is important condition')

    def __str__(self):
        return f'{super().__str__()}'

    def is_satisfied(self, user) -> bool:
        # TODO: implement
        return True
