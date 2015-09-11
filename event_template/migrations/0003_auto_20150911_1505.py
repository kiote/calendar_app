# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_template', '0002_auto_20150908_1506'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventtemplate',
            old_name='event_name',
            new_name='summary',
        ),
        migrations.AddField(
            model_name='eventtemplate',
            name='description',
            field=models.CharField(default=b'', max_length=4000),
        ),
        migrations.AddField(
            model_name='eventtemplate',
            name='location',
            field=models.URLField(default=b'http://www.path.to/study/website'),
        ),
        migrations.AlterField(
            model_name='eventtemplate',
            name='event_data_json',
            field=models.CharField(default=b'{}', max_length=4000),
        ),
    ]
