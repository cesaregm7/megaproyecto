# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-29 05:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id_test', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'test',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TestOrganizationGeneralForm',
            fields=[
                ('id_test_organization_general_form', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=6)),
                ('marital_status', models.CharField(max_length=45)),
                ('education', models.CharField(max_length=45)),
                ('job', models.CharField(max_length=45)),
                ('working_time', models.CharField(max_length=45)),
                ('organization_size', models.CharField(max_length=45)),
                ('organization_tipe', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'test_organization_general_form',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TestQuestions',
            fields=[
                ('id_test_questions', models.IntegerField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=150)),
                ('max_val', models.IntegerField()),
            ],
            options={
                'db_table': 'test_questions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id_test_result', models.IntegerField(primary_key=True, serialize=False)),
                ('resultado', models.TextField(blank=True, null=True)),
                ('generated_code', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'test_result',
                'managed': False,
            },
        ),
    ]