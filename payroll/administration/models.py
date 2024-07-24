from django.db import models
from django.utils import timezone

from dateutil.relativedelta import relativedelta


class Frequency(models.IntegerChoices):
    WEEKLY = 52, "Weekly"
    FORTNIGHTLY = 26, "Fortnightly"
    FOURWEEKLY = 13, "Fourweekly"
    MONTHLY = 12, "Monthly"
    QUARTERLY = 4, "Quarterly"
    ANNUAL = 1, "Annual"
    MANUAL = 0, "Manual"


class PayGroup(models.Model):
    code = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=50)
    frequency = models.IntegerField(
        "Standard Frequency",
        choices=Frequency.choices,
        default=Frequency.WEEKLY,
    )
    period_start = models.DateField("Base Period Start")
    period_end = models.DateField("Base Period End")
    pay_date = models.DateField("Base Pay Date")

    def __str__(self):
        return self.code

    def add_standard_pay(self):
        last_standard_pay = (
            PayPeriod.objects.filter(pay_group=self, frequency=self.frequency)
            .order_by("-period_end")
            .first()
        )
        if last_standard_pay:
            period_start = last_standard_pay.period_start
            period_end = last_standard_pay.period_end
            pay_date = last_standard_pay.pay_date
            match self.frequency:
                case Frequency.WEEKLY:
                    period_start = period_start + relativedelta(days=7)
                    period_end = period_end + relativedelta(days=7)
                    pay_date = pay_date + relativedelta(days=7)
                case Frequency.FORTNIGHTLY:
                    period_start = period_start + relativedelta(days=14)
                    period_end = period_end + relativedelta(days=14)
                    pay_date = pay_date + relativedelta(days=14)
                case Frequency.FOURWEEKLY:
                    period_start = period_start + relativedelta(days=28)
                    period_end = period_end + relativedelta(days=28)
                    pay_date = pay_date + relativedelta(days=28)
                case Frequency.MONTHLY:
                    period_start = period_start + relativedelta(months=1)
                    period_end = (
                        period_start + relativedelta(months=2) + relativedelta(days=-1)
                    )
                    pay_date = pay_date + relativedelta(months=1)
                case Frequency.QUARTERLY:
                    period_start = period_start + relativedelta(months=3)
                    period_end = (
                        period_start + relativedelta(months=4) + relativedelta(days=-1)
                    )
                    pay_date = pay_date + relativedelta(months=3)
                case Frequency.ANNUAL:
                    period_start = period_start + relativedelta(years=1)
                    period_end = period_end + relativedelta(years=1)
                    pay_date = pay_date + relativedelta(years=1)
                case _:
                    pass
        else:
            period_start = self.period_start
            period_end = self.period_end
            pay_date = self.pay_date
        standard_pay = PayPeriod.objects.create(
            pay_group=self,
            frequency=self.frequency,
            period_start=period_start,
            period_end=period_end,
            pay_date=pay_date,
        )
        return standard_pay

    def add_manual_pay(self):
        today = timezone.localtime(timezone.now()).date()
        manual_pay = PayPeriod.objects.create(
            pay_group=self,
            frequency=Frequency.MANUAL,
            period_start=today,
            period_end=today,
            pay_date=today,
        )
        return manual_pay


class PayPeriod(models.Model):
    pay_group = models.ForeignKey(PayGroup, on_delete=models.CASCADE)
    frequency = models.IntegerField(
        "Pay Frequency",
        choices=Frequency.choices,
        default=Frequency.WEEKLY,
    )
    period_start = models.DateField("Pay Period Start")
    period_end = models.DateField("Pay Period End")
    pay_date = models.DateField("Pay Date")

    def __str__(self):
        return f"{self.pay_group} - {self.period_start}"
