# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='catCompany',
            fields=[
                ('tblbdp_ptr', models.OneToOneField(to='main.tblBDP', parent_link=True, auto_created=True)),
                ('idCompany', models.AutoField(primary_key=True, serialize=False)),
                ('about', models.CharField(blank=True, null=True, max_length=1000)),
                ('mision', models.CharField(blank=True, null=True, max_length=500)),
                ('vision', models.CharField(blank=True, null=True, max_length=500)),
                ('target', models.CharField(blank=True, null=True, max_length=500)),
                ('isActive', models.BooleanField(default=1)),
                ('isMain', models.BooleanField(default=0)),
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
            ],
            bases=('main.tblbdp',),
        ),
        migrations.CreateModel(
            name='catEmployee',
            fields=[
                ('tblbdp_ptr', models.OneToOneField(to='main.tblBDP', parent_link=True, auto_created=True)),
                ('idEmployee', models.AutoField(primary_key=True, serialize=False)),
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
            ],
            bases=('main.tblbdp',),
        ),
        migrations.CreateModel(
            name='catMembership',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idMembership', models.AutoField(primary_key=True, serialize=False)),
                ('shortName', models.CharField(blank=True, null=True, max_length=10)),
                ('idCompany', models.ForeignKey(to='company.catCompany')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='tblCompanyHalls',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idCompany', models.ForeignKey(to='company.catCompany')),
                ('idHall', models.ForeignKey(to='main.catHalls')),
            ],
        ),
        migrations.CreateModel(
            name='tblDocument',
            fields=[
                ('idDocument', models.AutoField(primary_key=True, serialize=False)),
                ('methodPayment', models.IntegerField(choices=[(1, 'Efectivo'), (2, 'Cheque'), (3, 'Deposito'), (4, 'Otro')], default=1)),
                ('methodPaymentDetail', models.CharField(blank=True, null=True, max_length=200)),
                ('documentType', models.IntegerField(choices=[(1, 'Contado'), (2, 'Credito'), (3, 'Otro')], default=1)),
                ('credicState', models.IntegerField(choices=[(1, 'Pagado'), (2, 'Mora'), (3, 'Credito'), (4, 'Otro')], default=1)),
                ('discount', models.FloatField()),
                ('taxs', models.FloatField()),
                ('isNull', models.BooleanField(default=0)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idEmployee', models.ForeignKey(to='company.catEmployee')),
                ('idMembership', models.ForeignKey(to='company.catMembership')),
            ],
        ),
        migrations.CreateModel(
            name='tblEmployeeHistory',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idEmployeeHistory', models.AutoField(primary_key=True, serialize=False)),
                ('isActive', models.BooleanField(default=1)),
                ('idAppointment', models.ForeignKey(to='main.catAppointment')),
                ('idCompany', models.ForeignKey(to='company.catCompany')),
                ('idEmployee', models.ForeignKey(to='company.catEmployee')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='tlbDocumentDetailCredict',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idDocumentDetailCredict', models.AutoField(primary_key=True, serialize=False)),
                ('fee', models.FloatField()),
                ('methodPayment', models.IntegerField(choices=[(1, 'Efectivo'), (2, 'Cheque'), (3, 'Deposito'), (4, 'Otro')], default=1)),
                ('methodPaymentDetail', models.CharField(blank=True, null=True, max_length=200)),
                ('payment', models.FloatField()),
                ('programDate', models.DateField()),
                ('paymentDate', models.DateField(blank=True, null=True)),
                ('adjust', models.FloatField(blank=True, null=True)),
                ('adjustDetail', models.CharField(blank=True, null=True, max_length=200)),
                ('idDocument', models.ForeignKey(to='company.tblDocument')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='catemployee',
            name='history',
            field=models.ManyToManyField(through='company.tblEmployeeHistory', to='company.catCompany'),
        ),
        migrations.AddField(
            model_name='catcompany',
            name='halls',
            field=models.ManyToManyField(through='company.tblCompanyHalls', to='main.catHalls'),
        ),
    ]
