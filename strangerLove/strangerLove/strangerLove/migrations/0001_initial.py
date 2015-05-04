# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=5000)),
                ('date', models.DateTimeField()),
                ('location', models.TextField(max_length=5000)),
                ('numberOfPeopleNeeded', models.PositiveIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='owner',
            field=models.ForeignKey(related_name='owner', to='strangerLove.User'),
        ),
        migrations.AddField(
            model_name='attend',
            name='event',
            field=models.ForeignKey(related_name='participants', to='strangerLove.Event'),
        ),
        migrations.AddField(
            model_name='attend',
            name='user',
            field=models.ForeignKey(related_name='attendance', to='strangerLove.User'),
        ),
    ]
