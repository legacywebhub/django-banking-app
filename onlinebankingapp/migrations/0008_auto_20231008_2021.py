# Generated by Django 3.2.2 on 2023-10-08 19:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinebankingapp', '0007_auto_20231006_2018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='transaction_type',
        ),
        migrations.RemoveField(
            model_name='user',
            name='verified',
        ),
        migrations.AddField(
            model_name='loan',
            name='user_monthly_income',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='description',
            field=models.CharField(blank=True, choices=[('transfer', 'Transfer'), ('deposit', 'Deposit'), ('withdrawal', 'Withdrawal'), ('purchase', 'Purchase'), ('loan', 'Loan')], default='transfer', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='to_user',
            field=models.ForeignKey(blank=True, help_text='Recipient', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='receiver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='virtualcard',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
