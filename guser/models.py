from django.db import models
from django.utils import timezone

class Guser(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(default=timezone.now)
