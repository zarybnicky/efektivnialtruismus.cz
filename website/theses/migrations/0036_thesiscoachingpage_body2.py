# Generated by Django 2.2.1 on 2020-03-01 19:29

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('theses', '0035_auto_20191227_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='thesiscoachingpage',
            name='body2',
            field=wagtail.core.fields.StreamField([('rawHtml', wagtail.core.blocks.RawHTMLBlock()), ('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock())], blank=True, null=True),
        ),
    ]
