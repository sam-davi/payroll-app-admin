from django.db.models.signals import post_save
from django.dispatch import receiver

from employee.models import (
    Profile,
    Rate,
)
from company.models import RateType
from administration.choices import UnitTypes
from administration.mixins import EffectiveDateModel


@receiver(post_save)
def update_conflicts(sender, instance, created, **kwargs):
    """
    Signal handler for post model save to update
    conflicting model records
    """
    if issubclass(sender, EffectiveDateModel):
        instance.resolve_conflicts()
    if isinstance(instance, Profile):
        rate_type, _ = RateType.objects.get_or_create(
            code="DEFAULT", defaults={"description": "Default Hourly Rate"}
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
