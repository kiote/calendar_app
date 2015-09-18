from django.shortcuts import redirect
from django.views.generic import TemplateView

from oauth2client import client

from apiclient import errors
import logging


SCOPES = ['https://www.googleapis.com/auth/calendar', 'email', 'profile']


class HomeView(TemplateView):
    def get(self, request):
        if 'credentials' not in request.session:
            return redirect('callback')
        credentials = client.OAuth2Credentials.from_json(request.session['credentials'])
        if credentials.access_token_expired:
            return redirect('callback')
        else:
            return redirect('list')

class AuthView(TemplateView):
    def get(self, request):
        flow = client.flow_from_clientsecrets(
            'client_secrets.json',
            scope=' '.join(SCOPES),
            redirect_uri='https://gcalendar-api-events.herokuapp.com/oauth2callback')
        if 'code' not in request.GET:
            auth_uri = flow.step1_get_authorize_url()
            return redirect(auth_uri)
        else:
            auth_code = request.GET['code']
            credentials = flow.step2_exchange(auth_code)
            try:
                request.session['credentials'] = credentials.to_json()
            except errors.HttpError, e:
                logging.error('An error occurred: %s', e)
            return redirect('index')