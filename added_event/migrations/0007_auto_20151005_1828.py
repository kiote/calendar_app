# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('added_event', '0006_addedevent_time_start_changed_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addedevent',
            name='time_start_changed_to',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
