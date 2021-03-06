# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-01 21:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
        ('theses', '0013_thesisprovider_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThesisSearch',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.core.fields.StreamField((('rawHtml', wagtail.core.blocks.RawHTMLBlock()), ('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock())))),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='thesissimple',
            name='body',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock()), ('rawHtml', wagtail.core.blocks.RawHTMLBlock()), ('medailon', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(required=True)), ('pic', wagtail.images.blocks.ImageChooserBlock(required=True)), ('description', wagtail.core.blocks.RichTextBlock(required=True))), icon='user', template='blocks/medailon.html')))),
        ),
    ]
