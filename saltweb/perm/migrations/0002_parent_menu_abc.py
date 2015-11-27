# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent_menu',
            name='abc',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
    ]
