# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('added_event', '0005_addedevent_google_event_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='addedevent',
            name='time_start_changed_to',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 5, 18, 28, 21, 172510, tzinfo=utc)),
        ),
    ]
