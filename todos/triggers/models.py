from triggers.models import Action, Event, Condition
from django.utils.translation import gettext_lazy as _
from django.db import models


class TodoIsCompletedEvent(Event):

    class Meta(Event.Meta):
        verbose_name = _('todo is completed event')

    def __str__(self):
        return f'{super().__str__()}'


# @receiver(post_save, sender=Todo)
# def on_todo_created(sender, instance: Todo, created: bool, **kwargs):
#     event: TodoIsCompletedEvent
#     if instance.is_completed():
#         transaction.on_commit(lambda: [event.fire_single(
#             instance.user_id,
#         ) for event in TodoIsCompletedEvent.objects.all()])


class CreateTodoAction(Action):
    some = models.CharField(max_length=100, blank=True)

    class Meta(Action.Meta):
        verbose_name = _('create todo action')

    def __str__(self):
        return f'{super().__str__()} {self.some}'

    def perform(self, user, context):
        # TODO: implement
        print("made it!", user, context)


class TodoIsImportantCondition(Condition):
    class Meta(Condition.Meta):
        verbose_name = _('todo is important condition')

    def __str__(self):
        return f'{super().__str__()}'

    def is_satisfied(self, user) -> bool:
        # TODO: implement
        return True
