# Generated by Django 4.1.3 on 2022-12-07 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dgmallarticle',
            name='kategori',
            field=models.CharField(default=0, max_length=200),
        ),
    ]
