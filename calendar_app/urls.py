from django.conf.urls import include, url
from django.contrib import admin
from google_auth.views import AuthView
from event_template.views import SingleView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^oauth2callback/', AuthView.as_view(), name='callback'),
    url(r'^event/([0-9]+)/$', SingleView.as_view(), name='single_event'),
]
