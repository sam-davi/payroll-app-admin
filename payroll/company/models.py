from django.db import models


# Create your models here.
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

    def __str__(self):
        return self.display_name
