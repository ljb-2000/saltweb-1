# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perm', '0003_remove_parent_menu_abc'),
        ('user_manager', '0003_auto_20151019_0728'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='perm',
            field=models.ManyToManyField(to='perm.Sub_Menu'),
        ),
    ]
