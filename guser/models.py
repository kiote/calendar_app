from django.db import models
from django.utils import timezone

from apiclient import discovery

class Guser(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(default=timezone.now)

    @staticmethod
    def discover_email(http_auth):
        user_info_service = discovery.build(serviceName='oauth2',
                                            version='v2',
                                            http=http_auth)
        user_info = user_info_service.userinfo().get().execute()
        return user_info['email']
