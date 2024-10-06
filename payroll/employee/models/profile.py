from django.db import models

from administration.choices import UnitTypes, ConversionMethods
from administration.mixins import EmployeeEffectiveDateModel


class Profile(EmployeeEffectiveDateModel):
    rate = models.DecimalField(max_digits=12, decimal_places=4)
    unit_type = models.IntegerField(choices=UnitTypes.choices, default=UnitTypes.HOURLY)
    conversion_method = models.IntegerField(
        choices=ConversionMethods.choices, default=ConversionMethods.WEEKS
    )
    hours_per_week = models.DecimalField(max_digits=6, decimal_places=3, default=40)
    days_per_week = models.DecimalField(max_digits=6, decimal_places=3, default=5)

    class Meta(EmployeeEffectiveDateModel.Meta):
        pass

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
