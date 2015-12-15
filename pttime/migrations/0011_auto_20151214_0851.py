# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pttime', '0010_route_possible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='response',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='time',
            field=models.DurationField(null=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='transfers',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='walking_time',
            field=models.DurationField(null=True),
        ),
    ]
