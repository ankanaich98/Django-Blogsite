# Generated by Django 4.2.7 on 2023-12-06 09:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='image',
            field=models.ImageField(default='default.png', upload_to='post_pictures', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg'])]),
        ),
    ]