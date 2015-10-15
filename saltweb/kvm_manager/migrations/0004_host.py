# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kvm_manager', '0003_delete_host'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('saltkey', models.CharField(max_length=200)),
                ('hostname', models.CharField(max_length=100)),
                ('ip', models.IPAddressField(unique=True)),
                ('comment', models.TextField(max_length=500, blank=True)),
            ],
        ),
    ]
