# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 18:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Object',
            fields=[
                ('unique_identifier', models.AutoField(auto_created=True, help_text=b'A unique id used to create a bar code and identify the item.', primary_key=True, serialize=False)),
                ('registration_date', models.DateField(auto_now=True, help_text=b'The registration date of the item.')),
                ('title', models.CharField(default=b'', help_text=b'A title that briefly describes the object.', max_length=60)),
                ('description', models.TextField(default=b'', help_text=b'A longer initial description if necessary to specify the object in more detail.', max_length=1000)),
                ('transport', models.BooleanField(default=True, help_text=b'State whether the object should be transported or stay locally.')),
                ('entered_by', models.ForeignKey(default=None, help_text=b'The user entering this object!', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
