# Generated by Django 4.1.3 on 2022-12-06 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='student',
            field=models.TextField(default='test', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='unit',
            field=models.TextField(default='102', max_length=10),
            preserve_default=False,
        ),
    ]
