import os
import django
from added_event.models import AddedEvent

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "calendar_app.settings")
django.setup()

AddedEvent.objects.check_same()
