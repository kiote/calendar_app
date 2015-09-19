from oauth2client import client
import httplib2
from apiclient import discovery

from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import RequestContext
from django.contrib import messages
from django.shortcuts import redirect

from .models import EventTemplate
from guser.models import Guser
from added_event.models import AddedEvent

class ListView(TemplateView):
    def get(self, request):
        events = EventTemplate.objects.all()
        context = RequestContext(request, {'events': events})
        return render(request, 'event_template/index.html', context)

class SingleView(TemplateView):
    def get(self, request, event_id):
        """this action adds event to user's calendar"""
        if 'credentials' not in request.session:
            return redirect('callback')
        credentials = client.OAuth2Credentials.from_json(request.session['credentials'])
        if credentials.access_token_expired:
            return redirect('callback')
        http_auth = credentials.authorize(httplib2.Http())

        # add or create user to database
        user, created = Guser.objects.get_or_create(email=Guser.discover_email(http_auth))

        # create user attempt to add event to database
        event = EventTemplate.objects.get(id=event_id)
        AddedEvent.objects.create(guser=user, event=event)

        # call google api to create event
        event_json = event.event_data_json
        service = discovery.build('calendar', 'v3', http=http_auth)
        service.events().insert(calendarId='primary',
                                body=event_json).execute()
        messages.success(request, 'Event has been added to your calendar.')
        return redirect('list')