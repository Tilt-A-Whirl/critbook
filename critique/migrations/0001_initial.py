# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Critique',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=1)),
                ('text', models.CharField(max_length=250)),
                ('pos_x', models.IntegerField(default=0, verbose_name=b'x position')),
                ('pos_y', models.IntegerField(default=0, verbose_name=b'y position')),
                ('critique', models.ForeignKey(to='critique.Critique')),
            ],
        ),
    ]
