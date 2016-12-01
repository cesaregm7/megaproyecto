# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-10 03:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharedarea', '0003_induction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id_documents', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.TextField()),
                ('link', models.TextField()),
                ('keywords', models.TextField()),
                ('title', models.TextField()),
            ],
            options={
                'db_table': 'documents',
                'managed': False,
            },
        ),
    ]