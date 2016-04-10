# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='first_name',
            field=models.CharField(null=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='signup',
            name='last_name',
            field=models.CharField(null=True, max_length=120),
        ),
    ]
