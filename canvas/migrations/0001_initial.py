# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='FancyTitlePluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(help_text='Title to be displayed', max_length=60, verbose_name='Title')),
                ('top_margin', models.CharField(default=b'', choices=[(b'', b'None'), (b'sm', b'Small'), (b'md', b'Medium'), (b'lg', b'Large')], max_length=20, blank=True, help_text='Size of the margin top', verbose_name='Margin top')),
                ('center', models.BooleanField(default=False, help_text='Should the title be centered?', max_length=20, verbose_name='Centered')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='PromoPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('background', models.ImageField(help_text='The background of the promo box', upload_to=b'upload/promo_box/', verbose_name='Background image')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
