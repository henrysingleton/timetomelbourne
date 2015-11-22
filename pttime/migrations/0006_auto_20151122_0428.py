# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pttime', '0005_route'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name': 'Location Point'},
        ),
        migrations.AlterField(
            model_name='route',
            name='pain',
            field=models.IntegerField(blank=True),
        ),
    ]
