# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pttime', '0006_auto_20151122_0428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='pain',
            field=models.IntegerField(null=True),
        ),
    ]
