# Generated by Django 2.2.13 on 2020-06-17 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0002_question_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
