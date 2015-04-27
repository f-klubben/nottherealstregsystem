# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('username', models.CharField(blank=True, null=True, max_length=64)),
                ('name', models.CharField(default='', max_length=64)),
                ('number', models.IntegerField()),
                ('join_date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('_pin', models.CharField(verbose_name='pin', blank=True, null=True, max_length=128)),
                ('note', models.TextField(blank=True)),
                ('email', models.EmailField(max_length=75)),
                ('_phone_number', models.CharField(verbose_name='phone number', blank=True, max_length=16)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='list',
            name='members',
            field=models.ManyToManyField(to='fembers.Member'),
            preserve_default=True,
        ),
    ]
