# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('critique', '0002_remove_note_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='isCompleted',
            field=models.BooleanField(default=False),
        ),
    ]
