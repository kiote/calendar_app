import httplib2

from oauth2client import client
from apiclient import discovery
from datetime import timedelta
from datetime import datetime

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
    credentials = models.CharField(max_length=6000, default='')

    def __str__(self):
        return self.guser.email + ': ' + self.event.summary

    @staticmethod
    def check_same():
        """Check if event stays unchanged"""
        unchecked_events = AddedEvent.object.filter(checked=False)
        for event in unchecked_events:
            if event.was_cahged():
                event.changed = True
                event.save()

    def was_changed(self):
        # get current event info
        credentials = client.OAuth2Credentials.from_json(self.credentials)
        http_auth = credentials.authorize(httplib2.Http())
        service = discovery.build('calendar', 'v3', http=http_auth)
        remote_event = service.events().get(calendarId='primary',
                                            eventId=self.event_id).execute()

        # compare to event template
        internal_event = self.event
        if self.toUTC(remote_event['start']['dateTime']) != self.toUTC(internal_event.time_start):
            return True
        return False

    @staticmethod
    def toUTC(time):
        time_converted = datetime.strptime(time[0:19], '%Y-%m-%dT%H:%M:%S')

        if len(time) > 20:
            offset = int(time[-6:][0:3])
            time_converted -= timedelta(hours=offset)

        return time_converted
