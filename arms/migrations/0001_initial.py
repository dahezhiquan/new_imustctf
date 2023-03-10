# Generated by Django 3.2.16 on 2022-10-20 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='军火名称', max_length=255, unique=True)),
                ('introduction', models.CharField(help_text='简介', max_length=255)),
                ('label', models.CharField(help_text='标签【用分号隔开】', max_length=255)),
                ('details', models.TextField(help_text='详情', max_length=500)),
                ('type', models.CharField(help_text='类型', max_length=255)),
                ('created_time', models.DateTimeField(auto_now_add=True, help_text='创建时间')),
                ('img_src', models.TextField(help_text='图片链接', max_length=2000)),
                ('download_src', models.TextField(help_text='下载链接', max_length=2000)),
            ],
        ),
    ]
