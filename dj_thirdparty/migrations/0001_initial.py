# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('title', models.CharField(max_length=255, blank=True)),
                ('path', models.CharField(help_text=b'URL you want to use, python regular experssion, or constant "all"', max_length=255, blank=True)),
                ('css', models.TextField(blank=True)),
                ('javascript', models.TextField(blank=True)),
                ('active', models.BooleanField(default=True)),
                ('exact_match', models.BooleanField(default=True, help_text=b'Used when you want to add a code snippet to a specific page only.')),
                ('partial_match', models.BooleanField(default=False, help_text=b'Used when you want to add a code snippet to a lot of pages based on a regex.')),
                ('header', models.BooleanField(default=False, help_text=b'Set javascript to be in the head. Otherwise it will be in the footer')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
    ]
