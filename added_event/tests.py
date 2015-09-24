import json
import datetime
import mock

from django.test import TestCase
from django.utils import timezone

from event_template.models import EventTemplate
from guser.models import Guser
from .models import AddedEvent, AddedEventManager


event = EventTemplate.objects.create(summary='test_event')

class ServiceMock:
    def __init__(self, changed=True):
        self.changed = changed
        self.event = event

    def get(self, calendarId='', eventId=0):
        return self

    def execute(self):
        if self.changed:
            self.event.time_start = timezone.now() + datetime.timedelta(0, 10)
            self.event.save
        return json.loads(self.event.event_data_json)


class ServiceMockChangedEvent(ServiceMock):
    @staticmethod
    def events():
        return ServiceMock(True)


class ServiceMockUnchangedEvent(ServiceMock):
    @staticmethod
    def events():
        return ServiceMock(False)


class AddedEventTestCase(TestCase):
    def setUp(self):
        self.subject = AddedEvent.objects.create(event=event,
                                                 guser=Guser.objects.create(email='test@test.com'))

    @mock.patch('added_event.models.client')
    @mock.patch('added_event.models.discovery.build', lambda a, b, http='': ServiceMockUnchangedEvent())
    def test_was_changed_false(self, mock):
        self.assertFalse(self.subject.was_changed())

    @mock.patch('added_event.models.client')
    @mock.patch('added_event.models.discovery.build', lambda a, b, http='': ServiceMockChangedEvent())
    def test_was_changed_false(self, mock):
        self.assertTrue(self.subject.was_changed())


class AddedEventManagerTestCase(TestCase):
    def setUp(self):
        self.subject = AddedEvent.objects.create(summary='Hi')
