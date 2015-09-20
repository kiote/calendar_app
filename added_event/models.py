from django.db import models
from django.utils import timezone
from guser.models import Guser
from event_template.models import EventTemplate

class AddedEvent(models.Model):
    summary = models.CharField(max_length=2000)
    time_start = models.DateTimeField(default=timezone.now)
    time_end = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    guser = models.ForeignKey(Guser)
    event = models.ForeignKey(EventTemplate)
    updated_at = models.DateTimeField(default=timezone.now)
    checked = models.BooleanField(default=False)
    changed = models.BooleanField(default=False)
    credentials = models.CharField(max_length=2000)

    def __str__(self):
        return self.guser.email + ': ' + self.event.summary

    @staticmethod
    def check_same():
        unchecked_events = AddedEvent.object.filter(checked=False)
        for event in unchecked_events:
            pass