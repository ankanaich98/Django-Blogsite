# Generated by Django 5.0 on 2023-12-12 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_postsection_section_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postsection',
            old_name='section_content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='postsection',
            old_name='section_image',
            new_name='image',
        ),
    ]
