# Generated by Django 3.2.2 on 2023-09-19 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinebankingapp', '0002_auto_20230919_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='account_number',
            field=models.CharField(default='2107422611', max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='virtualcard',
            name='status',
            field=models.CharField(choices=[('null', 'Null'), ('pending', 'Pending'), ('declined', 'Declined'), ('active', 'Active'), ('inactive', 'Inactive'), ('expired', 'Expired')], default='null', max_length=10),
        ),
    ]
