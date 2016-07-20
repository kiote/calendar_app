# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('added_event', '0007_auto_20151005_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addedevent',
            name='time_start_changed_to',
            field=models.DateTimeField(),
        ),
    ]
