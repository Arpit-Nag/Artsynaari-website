# Generated by Django 2.2.16 on 2021-05-03 18:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_slot_request_slot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productrequest',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]