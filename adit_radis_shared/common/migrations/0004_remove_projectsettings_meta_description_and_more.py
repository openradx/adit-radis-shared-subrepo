# Generated by Django 5.0.4 on 2024-05-25 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_rename_siteprofile_projectsettings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectsettings',
            name='meta_description',
        ),
        migrations.RemoveField(
            model_name='projectsettings',
            name='meta_keywords',
        ),
        migrations.RemoveField(
            model_name='projectsettings',
            name='project_url',
        ),
        migrations.RemoveField(
            model_name='projectsettings',
            name='site',
        ),
    ]