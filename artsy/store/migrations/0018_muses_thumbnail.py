# Generated by Django 2.2.16 on 2021-08-06 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_auto_20210727_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='muses',
            name='thumbnail',
            field=models.FileField(blank=True, default=None, upload_to='muses_thumbnail/'),
        ),
    ]
