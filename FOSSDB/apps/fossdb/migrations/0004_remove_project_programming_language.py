# Generated by Django 4.2.2 on 2023-06-26 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fossdb', '0003_rename_proggramming_language_project_programming_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='programming_language',
        ),
    ]
