# Generated by Django 2.2.13 on 2020-06-17 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0008_auto_20200618_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
