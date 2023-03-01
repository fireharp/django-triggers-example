import logging
from triggers.models import Action, Event, Condition
from django.utils.translation import gettext_lazy as _
from django.db import models

logger = logging.getLogger(__name__)


class TodoIsFinishedEvent(Event):

    class Meta(Event.Meta):
        verbose_name = _('todo is finished event')

    def __str__(self):
        return f'{super().__str__()}'


class SendEmailAction(Action):
    email_message = models.TextField(_('email message'), blank=True)

    class Meta(Action.Meta):
        verbose_name = _('send email action')

    def __str__(self):
        return f'{super().__str__()} {self.email_message[:20]}'

    def perform(self, user, context):
        logger.debug(f"made it! {user} {context} {self.email_message[:50]}")


class UnfinishedTodosCountCondition(Condition):
    LOOKUP_EXACT = 'exact'
    LOOKUP_GTE = 'gte'
    LOOKUP_CHOICES = (
        (LOOKUP_EXACT, _('==')),
        (LOOKUP_GTE, _('>=')),
    )
    lookup = models.CharField(_('lookup'), choices=LOOKUP_CHOICES, max_length=8, default=LOOKUP_EXACT)
    value = models.PositiveIntegerField('value')

    class Meta(Condition.Meta):
        verbose_name = _('unfinished todos count condition')

    def __str__(self):
        return f'{super().__str__()}'

    def is_satisfied(self, user) -> bool:
        unfinished_todos_count = user.todos.filter(date_finished__isnull=True).count()
        if self.lookup == self.LOOKUP_EXACT:
            return unfinished_todos_count == self.value
        elif self.lookup == self.LOOKUP_GTE:
            return unfinished_todos_count >= self.value
        else:
            raise ValueError(f'Unknown lookup: {self.lookup}.')
