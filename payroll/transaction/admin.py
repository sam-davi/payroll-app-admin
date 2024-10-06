from django.contrib import admin

from .models import History, Current, Payslip


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = (
        "employee",
        "pay_period",
        "period_start",
        "period_end",
        "date",
        "allowance",
        "quantity",
        "unit",
        "hours",
        "days",
        "weeks",
        "rate",
        "rate_choices",
        "amount",
    )
    list_filter = ("pay_period", "period_end", "allowance")
    search_fields = (
        "employee__code",
        "employee__tax_number",
        "employee__first_name",
        "employee__last_name",
    )


@admin.register(Current)
class CurrentAdmin(admin.ModelAdmin):
    list_display = (
        "employee",
        "pay_period",
        "period_start",
        "period_end",
        "date",
        "allowance",
        "quantity",
        "unit",
        "hours",
        "days",
        "weeks",
        "rate",
        "rate_choices",
        "amount",
    )
    list_filter = ("pay_period", "period_end", "allowance")
    search_fields = (
        "employee__code",
        "employee__tax_number",
        "employee__first_name",
        "employee__last_name",
    )


@admin.register(Payslip)
class PayslipAdmin(admin.ModelAdmin):
    list_display = (
        "employee",
        "pay_period",
        "period_start",
        "period_end",
        "date",
        "allowance",
        "quantity",
        "unit",
        "hours",
        "days",
        "weeks",
        "rate",
        "rate_choices",
        "amount",
    )
    list_filter = ("pay_period", "period_end", "allowance")
    search_fields = (
        "employee__code",
        "employee__tax_number",
        "employee__first_name",
        "employee__last_name",
    )
