# Generated by Django 2.2.16 on 2021-07-12 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20210703_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='productrequest',
            name='size',
            field=models.CharField(choices=[('2XS', '2XS'), ('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('2XL', '2XL'), ('3XL', '3XL'), ('4XL', '4XL'), ('Made to measure', 'Made to measure')], max_length=50, null=True),
        ),
    ]
