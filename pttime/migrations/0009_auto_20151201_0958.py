# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pttime', '0008_route_score'),
    ]

    operations = [
        migrations.RenameField(
            model_name='route',
            old_name='xml_response',
            new_name='response',
        ),
    ]
