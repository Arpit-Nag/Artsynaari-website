# Generated by Django 2.2.16 on 2021-07-24 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_auto_20210721_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='ending_date',
            field=models.DateTimeField(default=None),
        ),
    ]
