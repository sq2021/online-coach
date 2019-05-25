# Generated by Django 2.2.1 on 2019-05-25 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qa', '0003_auto_20190525_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='author',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='is_solved',
            field=models.BooleanField(default=False, verbose_name='Is solved'),
        ),
    ]