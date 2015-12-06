# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pttime', '0007_auto_20151122_0430'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='score',
            field=models.IntegerField(null=True),
        ),
    ]
