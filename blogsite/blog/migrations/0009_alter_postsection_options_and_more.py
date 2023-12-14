# Generated by Django 5.0 on 2023-12-12 04:28

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_postmodel_image_alter_postsection_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postsection',
            options={'verbose_name': 'Post Section', 'verbose_name_plural': 'Post Sections'},
        ),
        migrations.RenameField(
            model_name='postsection',
            old_name='content',
            new_name='section_content',
        ),
        migrations.RenameField(
            model_name='postsection',
            old_name='image',
            new_name='section_image',
        ),
        migrations.RemoveField(
            model_name='postmodel',
            name='sections',
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='image',
            field=models.ImageField(default='default_post.png', upload_to='post_pictures', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg'])]),
        ),
        migrations.AlterField(
            model_name='postsection',
            name='post_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_sections', to='blog.postmodel', verbose_name='Post Model'),
        ),
    ]
