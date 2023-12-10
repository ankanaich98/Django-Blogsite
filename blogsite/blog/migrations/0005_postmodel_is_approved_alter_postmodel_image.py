# Generated by Django 4.2.7 on 2023-12-07 04:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_postmodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='image',
            field=models.ImageField(default='default_post.png', upload_to='post_pictures', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg'])]),
        ),
    ]