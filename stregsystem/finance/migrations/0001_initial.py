# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
        ('fembers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('member', models.ForeignKey(to='fembers.Member', blank=True, null=True)),
                ('product', models.ForeignKey(to='catalog.Product', blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
