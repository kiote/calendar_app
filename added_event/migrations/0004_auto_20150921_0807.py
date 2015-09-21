# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('added_event', '0003_addedevent_credentials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addedevent',
            name='credentials',
            field=models.CharField(default=b'', max_length=6000),
        ),
    ]
