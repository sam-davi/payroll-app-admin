from django.db import models

from datetime import time


def time_to_hours(time: time) -> float:
    return time.hour + time.minute / 60


class UnitType(models.TextChoices):
    HOURS = "H", "Hours"
    DAYS = "D", "Days"


class ShiftAllowance(models.Model):
    shift = models.ForeignKey("roster.Shift", on_delete=models.CASCADE)
    allowance = models.ForeignKey("company.Allowance", on_delete=models.CASCADE)
    unit_type = models.CharField(
        max_length=1, choices=UnitType.choices, default=UnitType.HOURS
    )
    rate_type = models.ForeignKey(
        "company.RateType", on_delete=models.SET_NULL, null=True, blank=True
    )

    @property
    def quantity(self):
        match self.unit_type:
            case UnitType.HOURS:
                return self.shift.paid_hours
            case UnitType.DAYS:
                return 1
            case _:
                return 0


class Shift(models.Model):
    name = models.CharField(max_length=50, unique=True)
    start_time = models.TimeField(default=time(8, 30))
    end_time = models.TimeField(default=time(17, 30))
    break_start = models.TimeField(default=time(12, 0))
    break_end = models.TimeField(default=time(12, 30))
    paid_break = models.BooleanField(default=False)
    rate_type = models.ForeignKey(
        "company.RateType", on_delete=models.SET_NULL, null=True, blank=True
    )
    allowances = models.ManyToManyField("company.Allowance", through=ShiftAllowance)

    def __str__(self):
        return self.name

    @property
    def start_time_hours(self):
        return time_to_hours(self.start_time)

    @property
    def end_time_hours(self):
        hours = time_to_hours(self.end_time)
        if self.end_time <= self.start_time:
            hours += 24
        return hours

    @property
    def break_start_hours(self):
        return time_to_hours(self.break_start)

    @property
    def break_end_hours(self):
        hours = time_to_hours(self.break_end)
        if self.break_end <= self.break_start:
            hours += 24
        return hours

    @property
    def total_hours(self):
        return self.end_time_hours - self.start_time_hours

    @property
    def break_hours(self):
        return (
            self.break_end_hours - self.break_start_hours
            if self.break_end_hours - self.break_start_hours < self.total_hours
            else 0
        )

    @property
    def paid_hours(self):
        return (
            self.total_hours if self.paid_break else self.total_hours - self.break_hours
        )
