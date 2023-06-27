# Generated by Django 4.2.2 on 2023-06-27 13:43

import account.models
from django.db import migrations, models
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_customuser_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(default=pathlib.PurePosixPath('profile_pic/default.jpg'), upload_to=account.models.get_profile_pic_path),
        ),
    ]
