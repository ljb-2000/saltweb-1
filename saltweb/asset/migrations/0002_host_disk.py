# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='disk',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
