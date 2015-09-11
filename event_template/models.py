from django.db import models
from django.utils import timezone
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

    def __str__(self):
        return self.summary
