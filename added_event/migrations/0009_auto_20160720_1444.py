# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('added_event', '0008_auto_20160720_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addedevent',
            name='time_start_changed_to',
            field=models.DateTimeField(null=True),
        ),
    ]
