# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='catBusinessContact',
            fields=[
                ('tblbdp_ptr', models.OneToOneField(to='main.tblBDP', parent_link=True, auto_created=True)),
                ('idBusinessContact', models.AutoField(primary_key=True, serialize=False)),
                ('isPerson', models.BooleanField(default=0)),
                ('isActive', models.BooleanField(default=1)),
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idAppointment', models.ForeignKey(to='main.catAppointment')),
            ],
            bases=('main.tblbdp',),
        ),
        migrations.CreateModel(
            name='catClient',
            fields=[
                ('tblbdp_ptr', models.OneToOneField(to='main.tblBDP', parent_link=True, auto_created=True)),
                ('idClient', models.AutoField(primary_key=True, serialize=False)),
                ('isPerson', models.BooleanField(default=0)),
                ('isActive', models.BooleanField(default=1)),
                ('beginDate', models.DateField(blank=True, null=True)),
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('contact', models.ManyToManyField(through='client.catBusinessContact', to='main.catAppointment')),
            ],
            bases=('main.tblbdp',),
        ),
        migrations.CreateModel(
            name='catKindClient',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idKindClient', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=35)),
                ('credictTimeAverage', models.PositiveIntegerField(blank=True, null=True, default=15)),
                ('credictAverage', models.FloatField(blank=True, null=True)),
                ('discountAverage', models.FloatField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='catclient',
            name='idKindClient',
            field=models.ForeignKey(to='client.catKindClient'),
        ),
        migrations.AddField(
            model_name='catbusinesscontact',
            name='idClient',
            field=models.ForeignKey(to='client.catClient'),
        ),
    ]
