# Generated by Django 4.0 on 2022-04-12 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0004_alter_article_publication_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='General', verbose_name='Slug'),
            preserve_default=False,
        ),
    ]
