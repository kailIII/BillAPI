# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('provider', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tblPurchase',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idPurchase', models.AutoField(primary_key=True, serialize=False)),
                ('noDocument', models.IntegerField()),
                ('idDocument', models.ForeignKey(to='company.tblDocument')),
                ('idProvider', models.ForeignKey(to='provider.catProvider')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
