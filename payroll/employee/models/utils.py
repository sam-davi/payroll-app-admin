from django.db import models

from datetime import date, timedelta

from administration.mixins import EffectiveDateModel


class EmployeeEffectiveDateModel(EffectiveDateModel):
    employee = models.ForeignKey("employee.Detail", on_delete=models.CASCADE)

    class Meta:
        abstract = True
        unique_together = ("employee", "effective_date")

    def get_matches(self):
        return self.__class__.objects.filter(employee=self.employee).exclude(id=self.id)
