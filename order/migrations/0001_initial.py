# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tblOrder',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idOrder', models.AutoField(primary_key=True, serialize=False)),
                ('validityDays', models.PositiveIntegerField(blank=True, null=True, default=15)),
                ('idClient', models.ForeignKey(to='client.catClient')),
                ('idDocument', models.ForeignKey(to='company.tblDocument')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
