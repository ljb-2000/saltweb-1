# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0003_auto_20151125_1143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='host',
            old_name='hosttype',
            new_name='kernel',
        ),
    ]
