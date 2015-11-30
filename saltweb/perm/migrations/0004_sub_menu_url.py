# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perm', '0003_remove_parent_menu_abc'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub_menu',
            name='url',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
