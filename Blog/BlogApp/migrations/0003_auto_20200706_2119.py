# Generated by Django 3.0.6 on 2020-07-06 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0002_auto_20200706_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=200),
        ),
    ]
