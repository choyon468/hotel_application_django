# Generated by Django 5.1.6 on 2025-03-04 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0002_alter_room_smoking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='bed_type',
            field=models.CharField(choices=[('', 'Select'), ('Single', 'Single'), ('Double', 'Double'), ('Queen', 'Queen'), ('King', 'King')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='room',
            name='smoking',
            field=models.CharField(choices=[('', 'Select'), ('Yes', 'Yes'), ('No', 'No')], default='', max_length=15),
        ),
    ]
