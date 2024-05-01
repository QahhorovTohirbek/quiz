# Generated by Django 5.0.4 on 2024-05-01 19:06

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_quiz_author_answer_answerdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='code',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='code',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='name',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='code',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='name',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
