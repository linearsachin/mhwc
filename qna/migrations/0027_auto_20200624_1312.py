# Generated by Django 2.2.13 on 2020-06-24 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0026_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
