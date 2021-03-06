# Generated by Django 2.2.16 on 2021-07-21 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_auto_20210719_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='muses',
            name='text',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.CreateModel(
            name='MusesImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='muses/')),
                ('model', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='store.Muses')),
            ],
        ),
    ]
