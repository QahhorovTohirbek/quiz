# Generated by Django 5.0.4 on 2024-05-05 12:55

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='name',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='name',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]