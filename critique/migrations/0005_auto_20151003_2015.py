# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('critique', '0004_critique_image_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='critique',
            name='image_file',
            field=models.ImageField(upload_to=b'crit_images/%Y/%m/%d', blank=True),
        ),
    ]
