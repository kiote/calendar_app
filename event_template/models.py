from django.db import models
from django.utils import timezone

class EventTemplate(models.Model):
    event_name = models.CharField(max_length=200)
    time_start = models.DateTimeField(default=timezone.now)
    time_end = models.DateTimeField(default=timezone.now)
    event_data_json = models.CharField(max_length=4000)
