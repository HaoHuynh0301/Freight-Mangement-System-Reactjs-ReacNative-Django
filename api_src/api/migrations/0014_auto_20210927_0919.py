# Generated by Django 3.2.6 on 2021-09-27 02:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_statusupdate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='statusupdate',
            options={'ordering': ['time']},
        ),
        migrations.AddField(
            model_name='request',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]