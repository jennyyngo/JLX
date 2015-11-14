# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GrubHunt', '0005_foodvendor_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foodvendor',
            old_name='users',
            new_name='userprofile',
        ),
    ]
