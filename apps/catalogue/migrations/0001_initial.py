# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields
import apps.catalogue.models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80, verbose_name='Brand name')),
                ('logo', sorl.thumbnail.fields.ImageField(help_text='Logo of this brand', upload_to=apps.catalogue.models.get_brand_logo_path, verbose_name='Logo')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.CharField(unique=True, max_length=255)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(max_length=45)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=60, verbose_name='Description')),
                ('item_order', models.PositiveIntegerField(default=0)),
                ('file', sorl.thumbnail.fields.ImageField(upload_to=apps.catalogue.models.get_product_photo_path)),
            ],
            options={
                'ordering': ['item_order'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=140, verbose_name='Product name')),
                ('description', models.TextField(verbose_name='Product description')),
                ('publication_date', models.DateField(help_text='Date when this product was published.', verbose_name='Publication date', auto_now_add=True)),
                ('visits', models.PositiveIntegerField(default=0, help_text='Number of times this product has been visited', verbose_name='Number of visit')),
                ('price', models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)),
                ('discount_price', models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)),
                ('slug', models.SlugField(help_text='A unique name to identify this product.', max_length=140, verbose_name='Slug')),
                ('brand', models.ForeignKey(blank=True, to='catalogue.Brand', null=True)),
                ('categories', models.ManyToManyField(help_text='Categories of this product', to='catalogue.Category', verbose_name='List of categories')),
                ('related_products', models.ManyToManyField(help_text='Products that are related to this product.', related_name='_product_related_products_+', verbose_name='List of related products', to='catalogue.Product', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductListPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('num_items', models.PositiveIntegerField(help_text=b'Number of items to be displayed', verbose_name='Number of items')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AddField(
            model_name='photo',
            name='product',
            field=models.ForeignKey(to='catalogue.Product'),
        ),
    ]
