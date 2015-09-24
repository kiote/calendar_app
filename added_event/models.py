import httplib2

from oauth2client import client
from apiclient import discovery
from datetime import timedelta
from datetime import datetime

from django.db import models
from django.utils import timezone

from guser.models import Guser
from event_template.models import EventTemplate

class AddedEventManager(models.Manager):
    def check_same(self):
        """Check if event stays unchanged"""
        unchecked_events = AddedEvent.objects.filter(checked=False)
        for event in unchecked_events:
            if event.was_changed():
                event.changed = True
                event.save()

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
    credentials = models.CharField(max_length=6000, default='')
    objects = AddedEventManager()
    google_event_id = models.CharField(max_length=2000, default='')

    def __str__(self):
        return self.guser.email + ': ' + self.event.summary

    def was_changed(self):
        # get current event info
        credentials = client.OAuth2Credentials.from_json(self.credentials)
        try:
            http_auth = credentials.authorize(httplib2.Http())
            service = discovery.build('calendar', 'v3', http=http_auth)
            remote_event = service.events().get(calendarId='primary',
                                                eventId=self.google_event_id).execute()
        except client.AccessTokenRefreshError:
            return False

        # compare to event template
        internal_event = self.event
        if self.toUTC(remote_event['start']['dateTime']) != self.toUTC(str(internal_event.time_start)):
            return True
        return False

    @staticmethod
    def toUTC(time):
        try:
            time_converted = datetime.strptime(time[0:19], '%Y-%m-%dT%H:%M:%S')
        except ValueError:
            time_converted = datetime.strptime(time[0:19], '%Y-%m-%d %H:%M:%S')

        if len(time) > 20:
            offset = int(time[-6:][0:3])
            time_converted -= timedelta(hours=offset)

        return time_converted
