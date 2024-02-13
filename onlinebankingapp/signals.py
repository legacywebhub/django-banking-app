from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, KYC, VirtualCard
from decimal import Decimal


# Creating KYC model for user
@receiver(post_save, sender=User)
def build_kyc(sender, instance, created, **kwargs):
    if created:
        KYC.objects.create(user=instance)

# Saving KYC model for user
@receiver(post_save, sender=User)
def save_kyc(sender, instance, **kwargs):
    instance.kyc.save()
