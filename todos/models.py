from django.db import models
from django.contrib.auth.models import User
from core.models import TimeStampedModel
from .triggers.models import TodoIsFinishedEvent


class Todo(TimeStampedModel):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    date_finished = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')

    def __str__(self):
        return self.title

    def is_finished(self):
        return bool(self.date_finished)

    def save(self, *args, **kwargs):
        fire_event = False
        if self.pk is not None:
            orig = Todo.objects.get(pk=self.pk)
            if orig.is_finished() != self.is_finished():
                fire_event = True
        super().save(*args, **kwargs)
        if fire_event:
            for event in TodoIsFinishedEvent.objects.all():
                event.fire_single(self.user_id)
