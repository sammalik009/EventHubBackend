# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-07 15:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
                ('method', models.CharField(max_length=10)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('received_amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
