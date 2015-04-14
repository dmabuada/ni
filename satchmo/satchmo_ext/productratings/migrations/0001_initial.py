# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_comments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductRating',
            fields=[
                ('comment', models.OneToOneField(primary_key=True, serialize=False, to='django_comments.Comment', verbose_name=b'Rating')),
                ('rating', models.IntegerField(verbose_name='Rating')),
            ],
        ),
    ]
