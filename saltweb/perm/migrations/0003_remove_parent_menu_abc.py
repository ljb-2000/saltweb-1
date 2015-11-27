# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perm', '0002_parent_menu_abc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent_menu',
            name='abc',
        ),
    ]
