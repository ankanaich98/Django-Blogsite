# Generated by Django 5.0 on 2023-12-11 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profilemodel_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('USER', 'User')], default='USER', max_length=20),
        ),
    ]
