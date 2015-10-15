# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kvm_manager', '0008_host'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Host',
        ),
    ]
