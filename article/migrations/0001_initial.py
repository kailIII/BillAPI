# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('main', '0001_initial'),
        ('provider', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='catArticle',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idArticle', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('codeBar', models.CharField(blank=True, null=True, max_length=100)),
                ('measureList', models.IntegerField(choices=[(1, 'gramos'), (2, 'Kilogramos'), (3, 'Onza'), (4, 'Libra'), (5, 'Litro'), (6, 'Galon'), (7, 'Quintal')], default=1)),
                ('measure', models.FloatField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='catBrand',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idBrand', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='catCompanyArticle',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idCompanyArticle', models.AutoField(primary_key=True, serialize=False)),
                ('idArticle', models.ForeignKey(to='article.catArticle')),
                ('idCompany', models.ForeignKey(to='company.catCompany')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='catModel',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idModel', models.AutoField(primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=35)),
                ('idBrand', models.ForeignKey(to='article.catBrand')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='catPresentation',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idPresentation', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='catProviderArticle',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idProviderArticle', models.AutoField(primary_key=True, serialize=False)),
                ('idArticle', models.ForeignKey(to='article.catArticle')),
                ('idProvider', models.ForeignKey(to='provider.catProvider')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='tblArticleDocumentDetails',
            fields=[
                ('idArticleDocumentDetails', models.AutoField(primary_key=True, serialize=False)),
                ('realPrice', models.FloatField(blank=True, null=True)),
                ('quantity', models.FloatField(null=True)),
                ('discount', models.FloatField()),
                ('tax', models.FloatField(blank=True, null=True)),
                ('idArticle', models.ForeignKey(to='article.catArticle')),
                ('idDocument', models.ForeignKey(to='company.tblDocument')),
            ],
        ),
        migrations.CreateModel(
            name='tblArticleHistoryPrice',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idArticleHistoryPrice', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.FloatField()),
                ('hasTax', models.BooleanField(default=0)),
                ('isActive', models.BooleanField(default=1)),
                ('idArticle', models.ForeignKey(to='article.catArticle')),
                ('idCoin', models.ForeignKey(to='main.catCoin')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='tblArticleInventory',
            fields=[
                ('idArticleInventory', models.AutoField(primary_key=True, serialize=False)),
                ('sMin', models.IntegerField()),
                ('sMax', models.IntegerField()),
                ('existence', models.IntegerField()),
                ('availability', models.IntegerField()),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idArticle', models.ForeignKey(to='article.catArticle')),
            ],
        ),
        migrations.CreateModel(
            name='tblArticlePresentation',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idArticlePresentation', models.AutoField(primary_key=True, serialize=False)),
                ('idArticle', models.ForeignKey(to='article.catArticle')),
                ('idPresentation', models.ForeignKey(to='article.catPresentation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='tblBatch',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idBatch', models.AutoField(primary_key=True, serialize=False)),
                ('noBatch', models.CharField(max_length=20)),
                ('createDate', models.DateField(blank=True, null=True)),
                ('expirationDate', models.DateField(blank=True, null=True)),
                ('quantity', models.PositiveIntegerField(blank=True, null=True)),
                ('isLapsed', models.BooleanField(default=0)),
                ('isActive', models.BooleanField(default=1)),
                ('idArticle', models.ForeignKey(to='article.catArticle')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='tblCategoryArticle',
            fields=[
                ('note', models.CharField(blank=True, null=True, max_length=255)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('idCategoryArticle', models.AutoField(primary_key=True, serialize=False)),
                ('idArticle', models.ForeignKey(to='article.catArticle')),
                ('idCategorySP', models.ForeignKey(to='main.catCategorySP')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='catpresentation',
            name='article',
            field=models.ManyToManyField(through='article.tblArticlePresentation', to='article.catArticle'),
        ),
        migrations.AddField(
            model_name='catarticle',
            name='category',
            field=models.ManyToManyField(through='article.tblCategoryArticle', to='main.catCategorySP'),
        ),
        migrations.AddField(
            model_name='catarticle',
            name='idModel',
            field=models.ForeignKey(to='article.catModel'),
        ),
    ]
