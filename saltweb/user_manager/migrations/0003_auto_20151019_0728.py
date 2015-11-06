# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_manager', '0002_auto_20151019_0728'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=80)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=75)),
                ('role', models.CharField(default=b'CU', max_length=2, choices=[(b'SU', b'SuperUser'), (b'CU', b'CommonUser')])),
                ('is_active', models.BooleanField(default=True)),
                ('last_login', models.DateTimeField(null=True)),
                ('date_joined', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=80)),
                ('comment', models.CharField(max_length=160, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.ManyToManyField(to='user_manager.UserGroup'),
        ),
    ]
