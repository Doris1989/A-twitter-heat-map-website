# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.BigIntegerField()),
                ('tid', models.BigIntegerField()),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('text', models.TextField(max_length=256)),
                ('time', models.DateField()),
                ('kwd', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
