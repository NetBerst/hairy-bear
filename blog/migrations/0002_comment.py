# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('autor', models.CharField(max_length=20)),
                ('message', models.TextField(max_length=100)),
                ('datetime', models.DateTimeField(verbose_name='Дата публикации', auto_now=True)),
                ('post', models.ForeignKey(to='blog.Post')),
            ],
        ),
    ]
