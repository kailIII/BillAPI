# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0001_initial'),
        ('company', '0001_initial'),
        ('main', '0001_initial'),
        ('provider', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='catCompanyService',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idCompanyService', models.AutoField(primary_key=True, serialize=False)),
                ('idCompany', models.ForeignKey(to='company.catCompany')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='catKindService',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idKindService', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='catProviderService',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idProviderArticle', models.AutoField(primary_key=True, serialize=False)),
                ('idProvider', models.ForeignKey(to='provider.catProvider')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='catService',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idService', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('shortname', models.CharField(blank=True, null=True, max_length=15)),
                ('duration', models.PositiveIntegerField(blank=True, null=True)),
                ('idKindService', models.ForeignKey(to='service.catKindService')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='tblCategoryServices',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idCategoryServices', models.AutoField(primary_key=True, serialize=False)),
                ('idCategorySP', models.ForeignKey(to='main.catCategorySP')),
                ('idService', models.ForeignKey(to='service.catService')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='tblScheduleDate',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idScheduleDate', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=90)),
                ('date', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='tblScheduleDateDetail',
            fields=[
                ('idScheduleDateDetail', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, null=True, max_length=90)),
                ('beginHour', models.TimeField(blank=True, null=True)),
                ('endHour', models.TimeField(blank=True, null=True)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idEmployee', models.ForeignKey(to='company.catEmployee')),
                ('idHall', models.ForeignKey(to='main.catHalls')),
                ('idScheduleDate', models.ForeignKey(to='service.tblScheduleDate')),
            ],
        ),
        migrations.CreateModel(
            name='tblServiceCost',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idServiceCost', models.AutoField(primary_key=True, serialize=False)),
                ('isActive', models.BooleanField(default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='tblServiceCostDetail',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idServiceCostDetail', models.AutoField(primary_key=True, serialize=False)),
                ('idPurchase', models.ForeignKey(to='purchase.tblPurchase')),
                ('idServiceCost', models.ForeignKey(to='service.tblServiceCost')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='tblServiceDocumentDetails',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idServiceDocumentDetails', models.AutoField(primary_key=True, serialize=False)),
                ('realPrice', models.FloatField(blank=True, null=True)),
                ('quantity', models.FloatField()),
                ('discount', models.FloatField(blank=True, null=True)),
                ('tax', models.FloatField(blank=True, null=True)),
                ('idDocument', models.ForeignKey(to='company.tblDocument')),
                ('idservice', models.ForeignKey(to='service.catService')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='tblServiceManage',
            fields=[
                ('idServiceManage', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.IntegerField(choices=[(1, 'Ejecucion'), (2, 'Preparacion'), (3, 'Culminado'), (4, 'Otro')], default=2)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idServiceCost', models.ForeignKey(to='service.tblServiceCost')),
            ],
        ),
        migrations.CreateModel(
            name='tblServicesHistoryPrice',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idServicesHistoryPrice', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.FloatField()),
                ('hasTax', models.BooleanField(default=0)),
                ('isActive', models.BooleanField(default=1)),
                ('idCoin', models.ForeignKey(to='main.catCoin')),
                ('idService', models.ForeignKey(to='service.catService')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='tblservicecost',
            name='idServiceDocumentDetails',
            field=models.ForeignKey(to='service.tblServiceDocumentDetails'),
        ),
        migrations.AddField(
            model_name='tblscheduledate',
            name='idServiceManage',
            field=models.ForeignKey(to='service.tblServiceManage'),
        ),
        migrations.AddField(
            model_name='catproviderservice',
            name='idService',
            field=models.ForeignKey(to='service.catService'),
        ),
        migrations.AddField(
            model_name='catcompanyservice',
            name='idService',
            field=models.ForeignKey(to='service.catService'),
        ),
    ]
