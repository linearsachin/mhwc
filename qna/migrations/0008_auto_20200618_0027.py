# Generated by Django 2.2.13 on 2020-06-17 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0007_reply_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forum_id', models.CharField(max_length=50, unique=True)),
                ('forum_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='slug',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='reply',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
