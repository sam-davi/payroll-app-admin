from django.db import models

from administration.mixins import EmployeeEffectiveDateModel


class Roster(EmployeeEffectiveDateModel):
    roster = models.ForeignKey("roster.Roster", on_delete=models.CASCADE)
    cycle_start = models.IntegerField()
    rate_type = models.ForeignKey(
        "company.RateType",
        related_name="employee_rosters",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta(EmployeeEffectiveDateModel.Meta):
        pass

    def __str__(self):
        return self.roster.name

    @property
    def repeating_unit(self):
        cycle_length = self.roster.cycle_length
        cycle_start = self.cycle_start
        hours_list = []
        for i in range(cycle_length):
            cycle_number = (i + cycle_start) % cycle_length
            shifts = self.roster.shifts.filter(rostershift__shift_number=cycle_number)
            hours_list.append(
                sum(shift.paid_hours for shift in shifts) if shifts else 0
            )
        return hours_list
