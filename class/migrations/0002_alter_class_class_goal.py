# Generated by Django 5.0.6 on 2024-06-17 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='class_goal',
            field=models.CharField(max_length=30),
        ),
    ]
