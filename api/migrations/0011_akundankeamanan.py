# Generated by Django 4.1.2 on 2023-01-17 07:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_articlesyariaharea'),
    ]

    operations = [
        migrations.CreateModel(
            name='AkundanKeamanan',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('master_judul', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('content_desc', models.TextField(blank=True, null=True)),
                ('is_active', models.SmallIntegerField(default=0)),
                ('image_link', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'pembeli_akun',
            },
        ),
    ]
