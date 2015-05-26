# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('datetime', models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)),
                ('content', models.TextField(max_length=10000)),
            ],
        ),
    ]
