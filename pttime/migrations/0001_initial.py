# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('postcode', models.IntegerField(max_length=4)),
                ('suburb', models.CharField(max_length=200)),
                ('landmark', models.CharField(max_length=200)),
                ('geolocation', djgeojson.fields.PointField()),
            ],
        ),
    ]
