from django.contrib import admin

from .models import Roster, RosterShift, Shift, ShiftAllowance


class ShiftAllowanceInline(admin.TabularInline):
    model = ShiftAllowance
    extra = 0


@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "start_time",
        "end_time",
        "total_hours",
        "paid_hours",
        "rate_type",
    )
    list_filter = ("start_time", "end_time")
    search_fields = ("name",)
    inlines = (ShiftAllowanceInline,)


class RosterShiftInline(admin.TabularInline):
    model = RosterShift
    extra = 0


@admin.register(Roster)
class RosterAdmin(admin.ModelAdmin):
    list_display = ("name", "cycle_length")
    list_filter = ("cycle_length",)
    search_fields = ("name",)
    inlines = (RosterShiftInline,)
