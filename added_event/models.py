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

    def __str__(self):
        self.guser.email + ': ' + self.event.summary