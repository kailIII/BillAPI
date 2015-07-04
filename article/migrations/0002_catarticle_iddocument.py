# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catarticle',
            name='idDocument',
            field=models.ManyToManyField(through='article.tblArticleDocumentDetails', to='company.tblDocument'),
        ),
    ]
