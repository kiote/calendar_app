# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('event_template', '0003_auto_20150911_1505'),
        ('guser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddedEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('summary', models.CharField(max_length=2000)),
                ('time_start', models.DateTimeField(default=django.utils.timezone.now)),
                ('time_end', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('event', models.ForeignKey(to='event_template.EventTemplate')),
                ('guser', models.ForeignKey(to='guser.Guser')),
            ],
        ),
    ]
