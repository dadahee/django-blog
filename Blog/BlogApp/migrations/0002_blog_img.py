# Generated by Django 3.0.6 on 2020-05-19 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='BlogApp/'),
        ),
    ]
