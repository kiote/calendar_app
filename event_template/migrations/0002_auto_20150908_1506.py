# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('event_template', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventtemplate',
            name='time_end',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='eventtemplate',
            name='time_start',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
