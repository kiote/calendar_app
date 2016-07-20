import httplib2
import json

from functools import wraps

from oauth2client import client
from apiclient import discovery

from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.utils import timezone

from event_template.models import EventTemplate
from guser.models import Guser
from added_event.models import AddedEvent


def _have_no_credentials(request):
    """Check if session has no credentials"""
    return 'credentials' not in request.session


def _get_credentials(request):
    return client.OAuth2Credentials.from_json(request.session['credentials'])


def set_session_event_id(function):
    """
    Sets eventId to session.

    We need this to be able to reirect back after login through google.
    """
    @wraps(function)
    def set_event_id(self, request, event_id):
        request.session['event_id'] = event_id
        return function(self, request, event_id)

    return set_event_id


def must_have_google_credentials(function):
    """
    Checks Google credentials.

    If we don't have them, or have expired, redirect to auth page
    """
    @wraps(function)
    def check_credentials(self, request, event_id):
        if _have_no_credentials(request):
            return redirect('callback')

        credentials = _get_credentials(request)

        if credentials.access_token_expired:
            return redirect('callback')

        return function(self, request, event_id)

    return check_credentials


class SingleView(TemplateView):
    @set_session_event_id
    @must_have_google_credentials
    def get(self, request, event_id):
        """this action adds event to user's calendar"""
        credentials = _get_credentials(request)
        http_auth = credentials.authorize(httplib2.Http())

        # add or create user into database
        email = Guser.discover_email(http_auth)
        user, created = Guser.objects.get_or_create(email=email)

        event = EventTemplate.objects.get(id=int(event_id))

        # call google api to create event
        event_json = json.loads(event.event_data_json)
        service = discovery.build('calendar', 'v3', http=http_auth)
        created_event = service.events().insert(calendarId='primary',
                                                body=event_json).execute()

        # create user attempt to add event to database
        AddedEvent.objects.create(guser=user,
                                  event=event,
                                  credentials=request.session['credentials'],
                                  google_event_id=created_event.get('id'),
                                  created_at=timezone.now())

        return redirect(created_event.get('htmlLink'))
