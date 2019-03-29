# Generated by Django 2.1.7 on 2019-03-14 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0020_copy_source_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='source_homepage',
        ),
        migrations.RemoveField(
            model_name='case',
            name='source_name',
        ),
        migrations.AlterField(
            model_name='case',
            name='source_url',
            field=models.URLField(help_text='Identifier of source object (URL for web pages, file names or IDs for corpora)', max_length=255),
        ),
    ]