# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pttime', '0002_auto_20151118_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='geolocation',
            field=djgeojson.fields.PointField(blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='postcode',
            field=models.IntegerField(),
        ),
    ]
