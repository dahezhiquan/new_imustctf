# Generated by Django 3.2.16 on 2022-10-22 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arms', '0002_rename_info_arms'),
    ]

    operations = [
        migrations.AddField(
            model_name='arms',
            name='watch',
            field=models.IntegerField(default=0, help_text='浏览数'),
        ),
    ]
