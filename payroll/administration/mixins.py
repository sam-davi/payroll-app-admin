from django.db import models

from datetime import date, timedelta


class EffectiveDateModel(models.Model):
    effective_date = models.DateField()
    effective_to = models.DateField(blank=True, default=date(9999, 12, 31))

    class Meta:
        abstract = True

    def get_matches(self):
        return self.__class__.objects.exclude(id=self.id)

    def resolve_conflicts(self):
        matches = self.get_matches()
        effective_to_fixes = matches.filter(
            effective_date__lte=self.effective_date,
            effective_to__gte=self.effective_date,
        )
        effective_from_fixes = matches.filter(
            effective_date__gte=self.effective_date,
            effective_date__lte=self.effective_to,
        )
        for match in effective_to_fixes:
            match.effective_to = self.effective_date - timedelta(days=1)
            match.save()
        if effective_from_fixes:
            self.effective_to = min(
                match.effective_date for match in effective_from_fixes
            ) - timedelta(days=1)
            self.save()


class EmployeeEffectiveDateModel(EffectiveDateModel):
    employee = models.ForeignKey("employee.Detail", on_delete=models.CASCADE)

    class Meta(EffectiveDateModel.Meta):
        abstract = True
        unique_together = ("employee", "effective_date")

    def get_matches(self):
        return (
            super(EmployeeEffectiveDateModel, self)
            .get_matches()
            .filter(employee=self.employee)
        )


class AdditionalDetailModel(EmployeeEffectiveDateModel):
    field = models.ForeignKey("company.CustomField", on_delete=models.CASCADE)

    class Meta(EmployeeEffectiveDateModel.Meta):
        abstract = True
        unique_together = ("employee", "field", "effective_date")

    def get_matches(self):
        return super(AdditionalDetailModel, self).get_matches().filter(field=self.field)

    def __str__(self):
        return f"{self.employee} - {self.field} - {self.effective_date} - {self.value}"
