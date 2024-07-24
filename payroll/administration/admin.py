from django.contrib import admin, messages
from django.utils.translation import ngettext

from .models import PayGroup, PayPeriod


@admin.register(PayGroup)
class PayGroupAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "description",
        "frequency",
        "period_start",
        "period_end",
        "pay_date",
    )
    list_filter = ("frequency",)
    search_fields = (
        "code",
        "description",
    )
    ordering = ("code",)

    actions = ["add_standard_pay", "add_manual_pay"]

    @admin.action(description="Add Standard Pay")
    def add_standard_pay(self, request, queryset):
        added = 0
        for pay_group in queryset:
            pay_group.add_standard_pay()
            added += 1
        self.message_user(
            request,
            ngettext("Added %d Standard Pay", "Added %d Standard Pays", added) % added,
            messages.SUCCESS,
        )

    @admin.action(description="Add Manual Pay")
    def add_manual_pay(self, request, queryset):
        added = 0
        for pay_group in queryset:
            pay_group.add_manual_pay()
            added += 1
        self.message_user(
            request,
            ngettext("Added %d Manual Pay", "Added %d Manual Pays", added) % added,
            messages.SUCCESS,
        )


@admin.register(PayPeriod)
class PayPeriodAdmin(admin.ModelAdmin):
    list_display = (
        "pay_group",
        "frequency",
        "period_start",
        "period_end",
        "pay_date",
    )
    list_filter = ("frequency",)
    search_fields = (
        "pay_group__code",
        "pay_group__description",
    )
    ordering = ("period_start",)
