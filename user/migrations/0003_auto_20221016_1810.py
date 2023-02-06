# Generated by Django 3.2.16 on 2022-10-16 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rename_user_info_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='vercode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(help_text='邮箱', max_length=255)),
                ('code', models.CharField(help_text='验证码', max_length=255)),
                ('last_modified', models.DateTimeField(auto_now=True, help_text='上次分发时间')),
            ],
        ),
        migrations.RemoveField(
            model_name='info',
            name='last_vercode',
        ),
    ]
