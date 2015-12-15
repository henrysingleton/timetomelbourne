# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pttime', '0009_auto_20151201_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='possible',
            field=models.BooleanField(default=True),
        ),
    ]
