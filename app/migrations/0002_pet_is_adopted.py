# Generated by Django 4.2.2 on 2023-10-06 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='is_adopted',
            field=models.BooleanField(default=False),
        ),
    ]