from django.db import models
from django.utils import timezone

from administration.mixins import EmployeeEffectiveDateModel


class Roster(EmployeeEffectiveDateModel):
    roster = models.ForeignKey("roster.Roster", on_delete=models.CASCADE)
    cycle_start = models.IntegerField()
    autopay = models.BooleanField(default=False)

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

    @property
    def current_shift_cycle(self):
        date = timezone.localtime(timezone.now()).date()
        return self.get_shift_cycle(date)

    @property
    def current_shifts(self):
        date = timezone.localtime(timezone.now()).date()
        return self.get_shifts(date)

    def get_shift_cycle(self, date):
        if date is None:
            raise ValueError("date cannot be None")
        cycle_length = self.roster.cycle_length
        cycle_start = self.cycle_start
        cycle_number = (date - self.effective_date).days % cycle_length
        return (cycle_number + cycle_start) % cycle_length

    def get_shifts(self, date):
        cycle_number = self.get_shift_cycle(date)
        shifts = self.roster.shifts.filter(rostershift__shift_number=cycle_number)
        return shifts
