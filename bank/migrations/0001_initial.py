# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='catBank',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idBank', models.AutoField(primary_key=True, serialize=False)),
                ('shortName', models.CharField(blank=True, null=True, max_length=30)),
                ('isActive', models.BooleanField(default=1)),
                ('idBDP', models.ForeignKey(to='main.tblBDP')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='tblBankControl',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idBankControl', models.AutoField(primary_key=True, serialize=False)),
                ('noAccount', models.CharField(max_length=40)),
                ('total', models.FloatField()),
                ('idBank', models.ForeignKey(to='bank.catBank')),
                ('idCoin', models.ForeignKey(to='main.catCoin')),
                ('idMembership', models.ForeignKey(to='company.catMembership')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='tblBankControlAdjust',
            fields=[
                ('idBankControlAdjust', models.AutoField(primary_key=True, serialize=False)),
                ('adjust', models.FloatField()),
                ('adjustDetail', models.CharField(max_length=255)),
                ('idBankControl', models.ForeignKey(to='bank.tblBankControl')),
            ],
        ),
        migrations.CreateModel(
            name='tblBankControlDetail',
            fields=[
                ('idBankControlDetail', models.AutoField(primary_key=True, serialize=False)),
                ('idBankControl', models.ForeignKey(to='bank.tblBankControl')),
                ('idDocument', models.ForeignKey(to='company.tblDocument')),
            ],
        ),
    ]
