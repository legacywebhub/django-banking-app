# Generated by Django 3.2.2 on 2023-09-28 23:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinebankingapp', '0003_auto_20230919_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='approved_date',
            field=models.DateTimeField(blank=True, help_text='This is the approved date of loan', null=True),
        ),
        migrations.AddField(
            model_name='loan',
            name='end_date',
            field=models.DateTimeField(blank=True, help_text='This field is calculated and depends on approved date and duration of loan', null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='from_user',
            field=models.ForeignKey(blank=True, help_text='Initiator', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='sender', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='to_user',
            field=models.ForeignKey(blank=True, help_text='Initiator', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='receiver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='account_number',
            field=models.CharField(default='7421591802', max_length=10, unique=True),
        ),
    ]
