from calendar_app.settings import HOST_NAME

from django.db import models
from django.utils import timezone
from django.core import urlresolvers

## {
#   'summary': 'Programming Task',
#   'location': 'http://www.path.to/study/website',
#   'description': 'A chance to hear more about Google\'s developer products.',
#   'start': {
#     'dateTime': '2015-09-28T06:00:00Z'
#   },
#   'end': {
#     'dateTime': '2015-09-28T06:30:00Z'
#   },
#   'attendees': [
#     {'email': 'study@studywebsite.com'}
#   ],
#   'reminders': {
#     'useDefault': False,
#     'overrides': [
#       {'method': 'email', 'minutes': 24 * 60},
#       {'method': 'popup', 'minutes': 10},
#     ],
#   },
# },


class EventTemplate(models.Model):
    summary = models.CharField(max_length=200)
    location = models.URLField(default='http://www.path.to/study/website')
    description = models.CharField(max_length=4000, default='')
    time_start = models.DateTimeField(default=timezone.now)
    time_end = models.DateTimeField(default=timezone.now)
    event_data_json = models.CharField(max_length=4000, default='{}')

    def link_to_event(self):
        host = HOST_NAME
        url = urlresolvers.reverse('single_event', args=(self.id,))
        return '{}{}'.format(host, url)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        instance = super(EventTemplate, self)
        self.event_data_json = self.to_json()
        instance.save()
        return instance

    def __str__(self):
        return self.summary

    def to_json(self):
        time_format = '%Y-%m-%dT%H:%M:%SZ'
        return '{"summary": "%s", "location": "%s", "description": "%s", "start": {"dateTime": "%s"}, "end": {"dateTime": "%s"}}' % \
            (self.summary, self.location, self.description, self.time_start.strftime(time_format), self.time_end.strftime(time_format))
