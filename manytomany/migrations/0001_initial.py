# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('friendly_name', models.CharField(max_length=200, verbose_name='Friendly name')),
                ('date_added', models.DateTimeField(default=datetime.datetime(2014, 12, 10, 15, 42, 54, 126657, tzinfo=utc))),
            ],
            options={
                'ordering': ['-date_added', 'friendly_name'],
                'verbose_name_plural': 'Properties',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('image_file', models.ImageField(upload_to=b'', verbose_name='Name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='property',
            name='images',
            field=models.ManyToManyField(to='manytomany.PropertyImage'),
            preserve_default=True,
        ),
    ]
