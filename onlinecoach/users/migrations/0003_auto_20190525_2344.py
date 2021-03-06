# Generated by Django 2.2.1 on 2019-05-26 03:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190525_2338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='reputation',
            new_name='reputation_count',
        ),
        migrations.AddField(
            model_name='customuser',
            name='total_answers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='total_questions',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user',
            field=models.OneToOneField(on_delete='models.CASCADE', to=settings.AUTH_USER_MODEL),
        ),
    ]
