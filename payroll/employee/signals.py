from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Detail, Profile, Rate, UnitTypes
from company.models import RateType


@receiver(post_save, sender=Profile)
def create_or_update_default_rate(sender, instance, created, **kwargs):
    """
    Signal handler for post Profile save to create or update Rate matching on
    employee, effective_date and rate_type__code = "default"
    """
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
