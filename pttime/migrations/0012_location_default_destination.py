# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pttime', '0011_auto_20151214_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='default_destination',
            field=models.BooleanField(default=False),
        ),
    ]
