import json
import mock

from mock import MagicMock

from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse

from .models import EventTemplate


def created_event_template(summary='Hi'):
    return EventTemplate.objects.create(summary=summary)


class EventTemplateTestCase(TestCase):
    def setUp(self):
        self.subject = created_event_template()

    def test_to_json(self):
        json_string = self.subject.to_json()
        self.assertTrue("Hi" in json_string)

    def test_event_data_json(self):
        self.assertTrue("Hi" in self.subject.event_data_json)


class SingleViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.event_template = created_event_template()
        self.event_id = self.event_template.id

    def test_get_with_no_credentials(self):
        response = self.client.get(reverse('single_event',
                                           args=(self.event_id,)))
        self.assertEquals(response.status_code, 302)

    @mock.patch('event_template.views.client.OAuth2Credentials.from_json')
    def test_get_with_access_token_expired(self, mock):
        session = self.client.session
        session['credentials'] = 'some credentials'
        session.save()

        mock.return_value = MagicMock(access_token_expired=True)

        response = self.client.get(reverse('single_event',
                                           args=(self.event_id,)))

        self.assertEquals(response.status_code, 302)
