# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('critique', '0006_auto_20151003_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='critique',
            name='height',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='critique',
            name='width',
            field=models.IntegerField(default=0, blank=True),
        ),
    ]
