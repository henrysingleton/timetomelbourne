# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pttime', '0003_auto_20151121_0316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='postcode',
            field=models.CharField(max_length=5, blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='suburb',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
