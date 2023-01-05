# Generated by Django 4.1.4 on 2023-01-03 05:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_articlepembeli'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticlePenjual',
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
                'db_table': 'article_penjual',
            },
        ),
    ]
