# Generated by Django 5.0 on 2023-12-12 08:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_postsection_post_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postsection',
            name='post_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.postmodel'),
        ),
    ]
