# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('added_event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addedevent',
            name='changed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='addedevent',
            name='checked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='addedevent',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
