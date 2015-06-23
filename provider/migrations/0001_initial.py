# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='catProvider',
            fields=[
                ('tblbdp_ptr', models.OneToOneField(to='main.tblBDP', parent_link=True, auto_created=True)),
                ('idProvider', models.AutoField(primary_key=True, serialize=False)),
                ('isPerson', models.BooleanField(default=0)),
                ('isActive', models.BooleanField(default=1)),
                ('beginDate', models.DateField(blank=True, null=True)),
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
            ],
            bases=('main.tblbdp',),
        ),
        migrations.CreateModel(
            name='tblProviderHalls',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idHall', models.ForeignKey(to='main.catHalls')),
                ('idProvider', models.ForeignKey(to='provider.catProvider')),
            ],
        ),
        migrations.AddField(
            model_name='catprovider',
            name='hall',
            field=models.ManyToManyField(through='provider.tblProviderHalls', to='main.catHalls'),
        ),
    ]
