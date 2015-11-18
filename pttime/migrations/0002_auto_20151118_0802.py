# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pttime', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='landmark',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
