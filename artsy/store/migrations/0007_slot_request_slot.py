# Generated by Django 2.2.16 on 2021-05-03 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20210503_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='request_slot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.ProductRequest'),
        ),
    ]
