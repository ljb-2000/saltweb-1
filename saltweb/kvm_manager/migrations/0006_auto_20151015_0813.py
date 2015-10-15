# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kvm_manager', '0005_auto_20151015_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='comment',
            field=models.TextField(max_length=500, blank=True),
        ),
    ]
