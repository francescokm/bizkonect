# Generated by Django 3.2.9 on 2021-12-02 07:35

import api_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=250, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_buyer', models.BooleanField(default=False)),
                ('is_seller', models.BooleanField(default=False)),
                ('profile_image', models.ImageField(blank=True, default=api_app.models.get_default_profile_image, null=True, upload_to=api_app.models.get_profile_image_filepath)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('languages', models.TextField(blank=True, null=True)),
                ('skills', models.TextField(blank=True, null=True)),
                ('education', models.CharField(blank=True, max_length=30, null=True)),
                ('certification', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
