# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GrubHunt', '0004_userprofile_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodvendor',
            name='users',
            field=models.ManyToManyField(to='GrubHunt.UserProfile'),
            preserve_default=True,
        ),
    ]
