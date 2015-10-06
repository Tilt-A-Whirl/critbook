# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('critique', '0003_note_iscompleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='critique',
            name='image_file',
            field=models.ImageField(null=True, upload_to=b'images/%Y/%m/%d', blank=True),
        ),
    ]
