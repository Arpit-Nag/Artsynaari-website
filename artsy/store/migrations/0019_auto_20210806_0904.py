# Generated by Django 2.2.16 on 2021-08-06 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_muses_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='muses',
            name='thumbnail',
            field=models.FileField(default=None, upload_to='muses_thumbnail/'),
        ),
    ]
