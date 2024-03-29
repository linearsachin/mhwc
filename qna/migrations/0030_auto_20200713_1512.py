# Generated by Django 2.2.13 on 2020-07-13 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0029_publicquestion_ip'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoodCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
            ],
            options={
                'verbose_name': 'MoodCheck',
                'verbose_name_plural': 'MoodChecks',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MoodQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name': 'MoodQ',
                'verbose_name_plural': 'MoodQs',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.RemoveField(
            model_name='reply',
            name='question',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Reply',
        ),
        migrations.AddField(
            model_name='moodcheck',
            name='mood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qna.MoodQ'),
        ),
    ]
