# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NugAccount', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nugaccount',
            name='balance',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='nugaccount',
            name='linkedAccount',
            field=models.TextField(default=b''),
        ),
    ]
