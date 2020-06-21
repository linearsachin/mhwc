# Generated by Django 2.2.13 on 2020-06-19 04:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qna', '0017_delete_forum'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='forum',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]