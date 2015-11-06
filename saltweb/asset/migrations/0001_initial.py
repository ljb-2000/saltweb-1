# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('saltkey', models.CharField(max_length=200)),
                ('hostname', models.CharField(max_length=100)),
                ('ip', models.IPAddressField(unique=True)),
                ('hosttype', models.CharField(max_length=100)),
                ('os', models.CharField(max_length=100)),
                ('cpunum', models.CharField(max_length=50)),
                ('cputype', models.CharField(max_length=100)),
                ('memory', models.CharField(max_length=100)),
                ('comment', models.TextField(max_length=500, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.IPAddressField(unique=True)),
                ('device', models.CharField(max_length=200)),
                ('comment', models.TextField(max_length=500, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.IPAddressField(unique=True)),
                ('device', models.CharField(max_length=200)),
                ('comment', models.TextField(max_length=500, blank=True)),
            ],
        ),
    ]
