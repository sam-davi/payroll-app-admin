from django.db import models

from company.models import FieldType


class Transaction(models.Model):
    employee = models.ForeignKey("employee.Detail", on_delete=models.CASCADE)
    pay_period = models.ForeignKey("administration.PayPeriod", on_delete=models.CASCADE)
    period_start = models.DateField()
    period_end = models.DateField()
    date = models.DateField()
    allowance = models.ForeignKey("company.Allowance", on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=12, decimal_places=4)
    unit = models.CharField(max_length=10, choices=FieldType.choices)
    hours = models.DecimalField(max_digits=12, decimal_places=4)
    days = models.DecimalField(max_digits=12, decimal_places=4)
    weeks = models.DecimalField(max_digits=12, decimal_places=4)
    rate = models.DecimalField(max_digits=12, decimal_places=4)
    rate_choices = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.employee} - {self.pay_period} - {self.date} - {self.allowance}"


class History(Transaction):
    pass


class Current(Transaction):
    pass


class Payslip(Transaction):
    pass
