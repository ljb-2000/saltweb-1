# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salt_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='module_name',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
