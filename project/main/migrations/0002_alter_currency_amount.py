# Generated by Django 4.2.15 on 2025-02-10 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='amount',
            field=models.FloatField(default=0),
        ),
    ]
