# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('critique', '0005_auto_20151003_2015'),
    ]

    operations = [
        migrations.AddField(
            model_name='critique',
            name='height',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='critique',
            name='width',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='critique',
            name='image_file',
            field=models.ImageField(height_field=b'height', width_field=b'width', max_length=200, upload_to=b'crit_images/%Y/%m/%d', blank=True),
        ),
    ]
