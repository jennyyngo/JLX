# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GrubHunt', '0002_route'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Route',
        ),
        migrations.AddField(
            model_name='foodvendor',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
    ]
