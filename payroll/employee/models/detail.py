from django.db import models

from datetime import date, timedelta

from administration.mixins import AdditionalDetailModel


class Detail(models.Model):
    code = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, default="")
    last_name = models.CharField(max_length=50, blank=True, default="")
    preferred_name = models.CharField(max_length=50, blank=True, default="")
    tax_number = models.CharField(max_length=9, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_hire = models.DateField(blank=True, null=True)
    date_of_termination = models.DateField(blank=True, default=date(9999, 12, 31))
    is_active = models.BooleanField(default=False)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    work_email = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.code

    @property
    def full_name(self):
        names = [self.first_name, self.middle_name, self.last_name]
        return " ".join([name for name in names if name])

    @property
    def short_name(self):
        names = [self.preferred_name or self.first_name, self.last_name]
        return " ".join([name for name in names if name])

    def time_since(self, reference_date):
        if not reference_date:
            return "Unknown"
        today = date.today()
        anniversary = reference_date.replace(year=today.year)
        if anniversary > today:
            anniversary = anniversary.replace(year=today.year - 1)
        days = today - anniversary
        return f"{anniversary.year - reference_date.year} years and {days.days} days"

    @property
    def age(self):
        return self.time_since(self.date_of_birth)

    @property
    def tenure(self):
        return self.time_since(self.date_of_hire)


class AdditionalDetail(AdditionalDetailModel):
    class Meta(AdditionalDetailModel.Meta):
        abstract = True


class AdditionalTextDetail(AdditionalDetail):
    field = models.ForeignKey("company.CustomTextField", on_delete=models.CASCADE)
    value = models.TextField()


class AdditionalNumberDetail(AdditionalDetail):
    field = models.ForeignKey("company.CustomNumberField", on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=12, decimal_places=4)


class AdditionalDateDetail(AdditionalDetail):
    field = models.ForeignKey("company.CustomDateField", on_delete=models.CASCADE)
    value = models.DateField()


class AdditionalBooleanDetail(AdditionalDetail):
    field = models.ForeignKey("company.CustomBooleanField", on_delete=models.CASCADE)
    value = models.BooleanField()
