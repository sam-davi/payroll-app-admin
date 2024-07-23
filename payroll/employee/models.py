from django.db import models

from datetime import date


# Create your models here.
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


class UnitTypes(models.IntegerChoices):
    HOURLY = 2080, "Hourly"
    DAILY = 260, "Daily"
    WEEKLY = 52, "Weekly"
    FORTNIGHTLY = 26, "Fortnightly"
    FOURWEEKLY = 13, "Fourweekly"
    MONTHLY = 12, "Monthly"
    ANNUAL = 1, "Annual"


class ConversionMethods(models.IntegerChoices):
    WEEKS = 364, "52 Weeks per Year"
    DAYS = 365, "365 Days per Year"


class Profile(models.Model):
    employee = models.ForeignKey("employee.Detail", on_delete=models.CASCADE)
    effective_date = models.DateField()
    rate = models.DecimalField(max_digits=12, decimal_places=4)
    unit_type = models.IntegerField(choices=UnitTypes.choices, default=UnitTypes.HOURLY)
    conversion_method = models.IntegerField(
        choices=ConversionMethods.choices, default=ConversionMethods.WEEKS
    )
    hours_per_week = models.DecimalField(max_digits=6, decimal_places=3, default=40)
    days_per_week = models.DecimalField(max_digits=6, decimal_places=3, default=5)

    class Meta:
        unique_together = ("employee", "effective_date")

    def __str__(self):
        return f"{self.employee} - {self.effective_date}"

    @property
    def hourly_rate(self):
        if self.unit_type == UnitTypes.HOURLY:
            return float(self.rate)
        return self.weekly_rate / float(self.hours_per_week)

    @property
    def daily_rate(self):
        if self.unit_type == UnitTypes.DAILY:
            return float(self.rate)
        return self.weekly_rate / float(self.days_per_week)

    @property
    def weekly_rate(self):
        match self.unit_type:
            case UnitTypes.WEEKLY:
                return float(self.rate)
            case UnitTypes.DAILY:
                return float(self.rate) * float(self.days_per_week)
            case UnitTypes.HOURLY:
                return float(self.rate) * float(self.hours_per_week)
            case UnitTypes.FORTNIGHTLY:
                return float(self.rate) * UnitTypes.FORTNIGHTLY / UnitTypes.WEEKLY
            case UnitTypes.FOURWEEKLY:
                return float(self.rate) * UnitTypes.FOURWEEKLY / UnitTypes.WEEKLY
            case UnitTypes.MONTHLY:
                return (
                    float(self.rate)
                    * (ConversionMethods.WEEKS / self.conversion_method)
                    * UnitTypes.MONTHLY
                    / UnitTypes.WEEKLY
                )
            case UnitTypes.ANNUAL:
                return (
                    float(self.rate)
                    * (ConversionMethods.WEEKS / self.conversion_method)
                    / UnitTypes.WEEKLY
                )

    @property
    def monthly_rate(self):
        match self.unit_type:
            case UnitTypes.MONTHLY:
                return float(self.rate)
            case UnitTypes.ANNUAL:
                return float(self.rate) / UnitTypes.MONTHLY
            case _:
                return (
                    self.weekly_rate
                    * (self.conversion_method / ConversionMethods.WEEKS)
                    * UnitTypes.WEEKLY
                    / UnitTypes.MONTHLY
                )

    @property
    def annual_rate(self):
        match self.unit_type:
            case UnitTypes.ANNUAL:
                return float(self.rate)
            case UnitTypes.MONTHLY:
                return float(self.rate) * UnitTypes.MONTHLY
            case _:
                return (
                    self.weekly_rate
                    * (self.conversion_method / ConversionMethods.WEEKS)
                    * UnitTypes.WEEKLY
                )


class Rate(models.Model):
    employee = models.ForeignKey("employee.Detail", on_delete=models.CASCADE)
    effective_date = models.DateField()
    rate_type = models.ForeignKey("company.RateType", on_delete=models.CASCADE)
    rate = models.DecimalField(max_digits=12, decimal_places=4)
    unit_type = models.IntegerField(choices=UnitTypes.choices, default=UnitTypes.HOURLY)

    class Meta:
        unique_together = ("employee", "effective_date", "rate_type")

    def __str__(self):
        return f"{self.employee} - {self.effective_date} - {self.rate_type}"
