# Generated by Django 2.2.13 on 2020-06-23 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0022_auto_20200621_0031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('is_og_blog', models.BooleanField(default=False)),
                ('author', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='publicquestion',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
