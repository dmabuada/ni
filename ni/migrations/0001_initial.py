# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='This is what the shop will be called in the default site language. To add non-default translations, use the Product Translation section below.', max_length=255, verbose_name='Name of shop')),
                ('slug', models.SlugField(help_text='Used for URLs, auto-generated from name if blank', max_length=255, verbose_name='Shop slug', blank=True)),
                ('short_description', models.TextField(default=b'', help_text='This should be a 1 or 2 line description in the default site language for use in product listing screens', max_length=200, verbose_name='Short description of shop', blank=True)),
                ('description', models.TextField(default=b'', help_text='This field can contain HTML and should be a few paragraphs in the default site language explaining the background of the shop.', verbose_name='Description of shop', blank=True)),
                ('meta', models.TextField(help_text='Meta description for this shop', max_length=200, null=True, verbose_name='Meta Description', blank=True)),
                ('date_added', models.DateField(null=True, verbose_name='Date added', blank=True)),
                ('active', models.BooleanField(default=True, help_text='This will determine whether or not this shop will appear on the homepage', verbose_name='Active')),
                ('featured', models.BooleanField(default=False, help_text='Featured items will show on the front page', verbose_name='Featured')),
                ('ordering', models.IntegerField(default=0, help_text='Override alphabetical order in category display', verbose_name='Ordering')),
                ('owner', models.ForeignKey(verbose_name='Owner', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(verbose_name='Site', to='sites.Site')),
            ],
            options={
                'ordering': ('site', 'ordering', 'name'),
                'verbose_name': 'Shop',
                'verbose_name_plural': 'Shops',
            },
        ),
        migrations.AlterUniqueTogether(
            name='shop',
            unique_together=set([('site', 'name'), ('site', 'slug')]),
        ),
    ]
