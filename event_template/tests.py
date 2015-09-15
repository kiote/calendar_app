from django.test import TestCase
from .models import EventTemplate
import json

class EventTemplateTestCase(TestCase):
    def setUp(self):
        self.subject = EventTemplate.objects.create(summary='Hi')

    def test_to_json(self):
        json_string = self.subject.to_json()
        self.assertTrue("Hi" in json_string)

    def test_event_data_json(self):
        self.assertTrue("Hi" in self.subject.event_data_json)
