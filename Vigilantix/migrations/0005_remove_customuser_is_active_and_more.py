# Generated by Django 4.1.6 on 2023-04-09 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vigilantix', '0004_policstation_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_superuser',
        ),
        migrations.AddField(
            model_name='customuser',
            name='aadhaar',
            field=models.IntegerField(null=True),
        ),
    ]
