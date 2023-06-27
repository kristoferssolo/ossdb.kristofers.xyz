# Generated by Django 4.2.2 on 2023-06-26 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HostingPlatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=50, unique=True)),
                ('full_name', models.CharField(max_length=100, unique=True)),
                ('url', models.URLField(blank=True, default='')),
                ('text', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='OperatingSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='OperatingSystemVersion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(blank=True, default='', max_length=50)),
                ('codename', models.CharField(blank=True, default='', max_length=100)),
                ('is_lts', models.BooleanField(blank=True, default=False)),
                ('operating_system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fossdb.operatingsystem')),
            ],
        ),
        migrations.CreateModel(
            name='ProgrammingLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, default='')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('license', models.ManyToManyField(blank=True, to='fossdb.license')),
                ('operating_system', models.ManyToManyField(blank=True, to='fossdb.operatingsystemversion')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='types/icons/')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectProgrammingLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.PositiveIntegerField()),
                ('programming_language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fossdb.programminglanguage')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fossdb.project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectHostingPlatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('hosting_platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fossdb.hostingplatform')),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fossdb.project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='tag',
            field=models.ManyToManyField(blank=True, to='fossdb.tag'),
        ),
    ]
