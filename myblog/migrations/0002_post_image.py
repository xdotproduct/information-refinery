# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-02 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FileField(default=True, upload_to=b''),
            preserve_default=False,
        ),
    ]