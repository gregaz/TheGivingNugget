# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NugAccount', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nugaccount',
            name='linkedAccount',
            field=models.TextField(default='default'),
            preserve_default=False,
        ),
    ]
