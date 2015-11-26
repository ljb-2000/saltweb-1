# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0002_host_disk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='disk',
            field=models.CharField(default='test', max_length=100),
            preserve_default=False,
        ),
    ]
