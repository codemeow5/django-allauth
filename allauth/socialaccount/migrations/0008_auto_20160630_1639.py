# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-30 08:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0007_socialaccount_social_app'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialaccount',
            name='social_app',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socialaccount.SocialApp', verbose_name=b'social app'),
        ),
    ]
