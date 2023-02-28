from django.db import models
from django.contrib.auth.models import User
from core.models import TimeStampedModel
from .triggers.models import TodoIsCompletedEvent


class Todo(TimeStampedModel):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    date_completed = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def is_completed(self):
        return bool(self.date_completed)

    # fire TodoIsCompletedEvent if todo is completed
    def save(self, *args, **kwargs):
        is_completed = self.is_completed()
        super().save(*args, **kwargs)

        if is_completed:
            event: TodoIsCompletedEvent
            for event in TodoIsCompletedEvent.objects.all():
                event.fire_single(self.user_id)
