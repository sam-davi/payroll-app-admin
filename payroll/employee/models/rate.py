from django.db import models

from administration.choices import UnitTypes
from administration.mixins import EmployeeEffectiveDateModel


class Rate(EmployeeEffectiveDateModel):
    rate_type = models.ForeignKey("company.RateType", on_delete=models.CASCADE)
    rate = models.DecimalField(max_digits=12, decimal_places=4)
    unit_type = models.IntegerField(choices=UnitTypes.choices, default=UnitTypes.HOURLY)

    class Meta(EmployeeEffectiveDateModel.Meta):
        unique_together = ("employee", "effective_date", "rate_type")

    def get_matches(self):
        return super(Rate, self).get_matches().filter(rate_type=self.rate_type)

    def __str__(self):
        return f"{self.employee} - {self.effective_date} - {self.rate_type}"
