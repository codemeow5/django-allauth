# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 04:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0006_socialapp_mch_appkey'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialaccount',
            name='social_app',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='socialaccount.SocialApp', verbose_name=(b'social app',)),
            preserve_default=False,
        ),
    ]
