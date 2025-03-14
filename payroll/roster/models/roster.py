from django.db import models


class Roster(models.Model):
    name = models.CharField(max_length=50, unique=True)
    cycle_length = models.IntegerField(default=7)
    shifts = models.ManyToManyField("roster.Shift", through="roster.RosterShift")

    def __str__(self):
        return self.name


class RosterShift(models.Model):
    roster = models.ForeignKey(Roster, on_delete=models.CASCADE)
    shift = models.ForeignKey("roster.Shift", on_delete=models.CASCADE)
    shift_number = models.IntegerField()

    def __str__(self):
        return str(self.roster)

    class Meta:
        unique_together = (
            "roster",
            "shift",
            "shift_number",
        )
