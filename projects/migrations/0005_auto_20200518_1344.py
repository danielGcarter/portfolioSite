# Generated by Django 3.0.4 on 2020-05-18 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20200517_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path='D:\\Projects\\Portfolio\\portfolio\\static'),
        ),
    ]
