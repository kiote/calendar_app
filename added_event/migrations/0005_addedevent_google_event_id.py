# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('added_event', '0004_auto_20150921_0807'),
    ]

    operations = [
        migrations.AddField(
            model_name='addedevent',
            name='google_event_id',
            field=models.CharField(default=b'', max_length=2000),
        ),
    ]
