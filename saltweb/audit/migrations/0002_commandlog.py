# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommandLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exec_time', models.DateTimeField()),
                ('username', models.CharField(max_length=100)),
                ('exec_moudle', models.CharField(max_length=100)),
                ('exec_args', models.CharField(max_length=200)),
            ],
        ),
    ]
