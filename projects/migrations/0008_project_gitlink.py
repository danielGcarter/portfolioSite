# Generated by Django 3.0.4 on 2020-05-18 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20200518_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='gitLink',
            field=models.TextField(default=''),
        ),
    ]