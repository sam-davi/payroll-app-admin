from django.db import models

from datetime import date, timedelta

from administration.choices import UnitTypes
from administration.mixins import EffectiveDateModel


class Detail(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)
    tax_number = models.CharField(max_length=9, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.code


class RateType(models.Model):
    code = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.code


class RateTypeDefault(EffectiveDateModel):
    rate_type = models.ForeignKey(RateType, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=12, decimal_places=4)
    unit_type = models.IntegerField(choices=UnitTypes.choices, default=UnitTypes.HOURLY)

    class Meta(EffectiveDateModel.Meta):
        unique_together = (
            "rate_type",
            "effective_date",
        )

    def get_matches(self):
        return (
            super(RateTypeDefault, self).get_matches().filter(rate_type=self.rate_type)
        )


class FieldType(models.TextChoices):
    HOURS = "HOURS", "Hours"
    DAYS = "DAYS", "Days"
    WEEKS = "WEEKS", "Weeks"
    QUANTITY = "QUANTITY", "Quantity"
    AMOUNT = "AMOUNT", "Amount"


class Accumulator(models.Model):
    code = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=50)
    field_type = models.CharField(
        max_length=10, choices=FieldType.choices, default=FieldType.AMOUNT
    )

    def __str__(self):
        return self.code


class AllowanceType(models.Model):
    code = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=50)
    accumulators = models.ManyToManyField(
        Accumulator, through="AccumulatorMember", blank=True
    )

    def __str__(self):
        return self.code


class AccumulatorMember(models.Model):
    allowance_type = models.ForeignKey(AllowanceType, on_delete=models.CASCADE)
    accumulator = models.ForeignKey(Accumulator, on_delete=models.CASCADE)

    class Meta:
        unique_together = (
            "allowance_type",
            "accumulator",
        )

    def __str__(self):
        return f"{self.accumulator}: {self.allowance_type}"


class Allowance(models.Model):
    code = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=50)
    display_name = models.CharField(max_length=50)
    allowance_type = models.ForeignKey(AllowanceType, on_delete=models.CASCADE)
    unit_type = models.CharField(
        max_length=10, choices=FieldType.choices, default=FieldType.HOURS
    )

    def __str__(self):
        return self.display_name


class CustomField(models.Model):
    field_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.field_name

    class Meta:
        abstract = True


class CustomDateField(CustomField):
    pass


class CustomNumberField(CustomField):
    pass


class CustomTextField(CustomField):
    pass
