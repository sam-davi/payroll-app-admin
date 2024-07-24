from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import (
    AdditionalDateDetail,
    AdditionalNumberDetail,
    AdditionalTextDetail,
    Profile,
    Rate,
    UnitTypes,
)
from company.models import RateType


@receiver(post_save, sender=Profile)
def create_or_update_default_rate(sender, instance, created, **kwargs):
    """
    Signal handler for post Profile save to create or update Rate matching on
    employee, effective_date and rate_type__code = "default"
    """
    instance.resolve_conflicts()
    rate_type, _ = RateType.objects.get_or_create(
        code="default", defaults={"description": "Default Hourly Rate"}
    )
    defaults = {
        "rate": instance.hourly_rate,
        "unit_type": UnitTypes.HOURLY,
    }
    Rate.objects.update_or_create(
        employee=instance.employee,
        effective_date=instance.effective_date,
        rate_type=rate_type,
        defaults=defaults,
    )


@receiver(post_save, sender=Rate)
def update_rate_conflicts(sender, instance, created, **kwargs):
    """
    Signal handler for post AdditionalDateDetail save to update
    conflicting AdditionalDateDetail records
    """
    instance.resolve_conflicts()


@receiver(post_save, sender=AdditionalDateDetail)
def update_additional_date_conflicts(sender, instance, created, **kwargs):
    """
    Signal handler for post AdditionalDateDetail save to update
    conflicting AdditionalDateDetail records
    """
    instance.resolve_conflicts()


@receiver(post_save, sender=AdditionalNumberDetail)
def update_additional_date_conflicts(sender, instance, created, **kwargs):
    """
    Signal handler for post AdditionalNumberDetail save to update
    conflicting AdditionalNumberDetail records
    """
    instance.resolve_conflicts()


@receiver(post_save, sender=AdditionalTextDetail)
def update_additional_date_conflicts(sender, instance, created, **kwargs):
    """
    Signal handler for post AdditionalTextDetail save to update
    conflicting AdditionalTextDetail records
    """
    instance.resolve_conflicts()
