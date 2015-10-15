# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kvm_manager', '0006_auto_20151015_0813'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Host',
        ),
    ]
