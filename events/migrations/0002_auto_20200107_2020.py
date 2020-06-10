# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-07 15:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
        ('payment', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.Payment'),
        ),
        migrations.AddField(
            model_name='registration',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User'),
        ),
        migrations.AddField(
            model_name='imagetable',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event'),
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User'),
        ),
    ]