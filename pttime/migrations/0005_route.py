# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pttime', '0004_auto_20151121_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('transfers', models.IntegerField()),
                ('time', models.DurationField()),
                ('walking_time', models.DurationField()),
                ('pain', models.IntegerField()),
                ('xml_response', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('destination', models.ForeignKey(to='pttime.Location', related_name='destination')),
                ('origin', models.ForeignKey(to='pttime.Location', related_name='origin')),
            ],
        ),
    ]
