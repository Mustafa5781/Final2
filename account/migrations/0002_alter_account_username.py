# Generated by Django 5.1.6 on 2025-02-10 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=30, unique=True, verbose_name='Full Name'),
        ),
    ]
