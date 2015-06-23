# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='catAddress',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idAddress', models.AutoField(primary_key=True, serialize=False)),
                ('kind', models.IntegerField(choices=[(1, 'Principal'), (2, 'Secundaria'), (3, 'Otra')], default=1)),
                ('address', models.CharField(max_length=255)),
                ('isActive', models.BooleanField(default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='catAppointment',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idAppointment', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='catArea',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idArea', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('shortName', models.CharField(blank=True, null=True, max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='catCategorySP',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idCategorySP', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='catCity',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idCity', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=75)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='catCoin',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idCoin', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=35)),
                ('symbol', models.CharField(max_length=4)),
                ('isMain', models.BooleanField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='catCountry',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idCountry', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.PositiveIntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=75)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='catHalls',
            fields=[
                ('idHall', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=255)),
                ('beginHour', models.TimeField(blank=True, null=True)),
                ('endHour', models.TimeField(blank=True, null=True)),
                ('state', models.IntegerField(choices=[(1, 'Libre'), (2, 'Ocupado'), (3, 'Mantenimiento'), (4, 'Otro')], default=1)),
                ('idCity', models.ForeignKey(to='main.catCity')),
            ],
        ),
        migrations.CreateModel(
            name='catMail',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idMail', models.AutoField(primary_key=True, serialize=False)),
                ('kind', models.IntegerField(choices=[(1, 'Private'), (2, 'Public'), (3, 'Coorporative')])),
                ('mail', models.CharField(max_length=40)),
                ('isActive', models.BooleanField(default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='catPhone',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idPhone', models.AutoField(primary_key=True, serialize=False)),
                ('kind', models.IntegerField(choices=[(1, 'Movil'), (2, 'Fijo')], default=1)),
                ('scope', models.IntegerField(choices=[(1, 'Casa'), (2, 'Trabajo'), (3, 'Principal'), (4, 'Otro')], default=1)),
                ('area', models.PositiveIntegerField(blank=True, null=True)),
                ('number', models.IntegerField()),
                ('isActive', models.BooleanField(default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='catWebsite',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idWebsite', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, null=True, max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('isActive', models.BooleanField(default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='tblBDP',
            fields=[
                ('idBDP', models.AutoField(primary_key=True, serialize=False)),
                ('photo', models.CharField(blank=True, null=True, max_length=255)),
                ('idCard', models.CharField(blank=True, null=True, max_length=25)),
                ('postal', models.PositiveIntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=75)),
                ('surname', models.CharField(max_length=75)),
                ('birthdate', models.DateField()),
                ('idAddress', models.ManyToManyField(through='main.catAddress', to='main.catCity')),
            ],
        ),
        migrations.CreateModel(
            name='tblCoinHistory',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idCoinHistory', models.AutoField(primary_key=True, serialize=False)),
                ('rateChange', models.FloatField()),
                ('isActive', models.BooleanField(default=1)),
                ('idCoin', models.ForeignKey(to='main.catCoin')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='catwebsite',
            name='idBDP',
            field=models.ForeignKey(to='main.tblBDP'),
        ),
        migrations.AddField(
            model_name='catphone',
            name='idBDP',
            field=models.ForeignKey(to='main.tblBDP'),
        ),
        migrations.AddField(
            model_name='catmail',
            name='idBDP',
            field=models.ForeignKey(to='main.tblBDP'),
        ),
        migrations.AddField(
            model_name='catcoin',
            name='idCountry',
            field=models.ForeignKey(to='main.catCountry'),
        ),
        migrations.AddField(
            model_name='catcity',
            name='idcountry',
            field=models.ForeignKey(to='main.catCountry'),
        ),
        migrations.AddField(
            model_name='catappointment',
            name='idArea',
            field=models.ForeignKey(to='main.catArea'),
        ),
        migrations.AddField(
            model_name='cataddress',
            name='idBDP',
            field=models.ForeignKey(to='main.tblBDP'),
        ),
        migrations.AddField(
            model_name='cataddress',
            name='idCity',
            field=models.ForeignKey(to='main.catCity'),
        ),
    ]
