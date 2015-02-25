# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('active', models.BooleanField(default=True)),
                ('username', models.CharField(max_length=16)),
                ('year', models.CharField(max_length=4)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('U', 'Unknown'), ('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('email', models.EmailField(blank=True, max_length=75)),
                ('want_spam', models.BooleanField(default=True)),
                ('balance', models.IntegerField(default=0)),
                ('undo_count', models.IntegerField(default=0)),
                ('phone_number', models.CharField(blank=True, max_length=16)),
                ('notes', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=40)),
                ('text', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('stop_date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OldPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('price', models.IntegerField()),
                ('changed_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField()),
                ('member', models.ForeignKey(to='stregsystem.Member')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('price', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('deactivate_date', models.DateTimeField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('price', models.IntegerField()),
                ('member', models.ForeignKey(to='stregsystem.Member')),
                ('product', models.ForeignKey(to='stregsystem.Product')),
                ('room', models.ForeignKey(to='stregsystem.Room', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='oldprice',
            name='product',
            field=models.ForeignKey(related_name='old_prices', to='stregsystem.Product'),
            preserve_default=True,
        ),
    ]
