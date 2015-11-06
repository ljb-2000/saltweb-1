# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cobbler_Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(max_length=200)),
                ('interface', models.CharField(max_length=50)),
                ('ip', models.IPAddressField()),
                ('gateway', models.IPAddressField()),
                ('dns', models.IPAddressField()),
                ('mac', models.CharField(max_length=100)),
                ('profile', models.CharField(max_length=500)),
                ('user', models.CharField(max_length=100)),
                ('date_joined', models.DateTimeField(null=True)),
            ],
        ),
    ]
