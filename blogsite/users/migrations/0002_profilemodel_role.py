# Generated by Django 5.0 on 2023-12-09 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('USER', 'User')], default='User', max_length=20),
        ),
    ]
