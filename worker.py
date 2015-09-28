import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "calendar_app.settings")
django.setup()

from added_event.models import AddedEvent

AddedEvent.objects.check_same()