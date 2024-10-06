from django.contrib import admin

from .models import (
    AdditionalDateDetail,
    AdditionalNumberDetail,
    AdditionalTextDetail,
    Detail,
    Profile,
    Rate,
    Roster,
)


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = (
        "employee",
        "effective_date",
        "effective_to",
        "rate_type",
        "rate",
        "unit_type",
    )
    list_filter = ("employee", "rate_type", "unit_type")
    search_fields = (
        "employee__code",
        "employee__tax_number",
        "employee__first_name",
        "employee__last_name",
    )
    ordering = ("employee__code", "effective_date", "rate_type")


class RateInline(admin.TabularInline):
    model = Rate
    extra = 0


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "employee",
        "effective_date",
        "hours_per_week",
        "days_per_week",
        "conversion_method",
        "hourly_rate",
        "weekly_rate",
        "monthly_rate",
        "annual_rate",
    )
    list_filter = ("unit_type", "conversion_method")
    search_fields = (
        "employee__code",
        "employee__tax_number",
        "employee__first_name",
        "employee__last_name",
    )
    ordering = ("employee__code", "effective_date")


class ProfileInline(admin.TabularInline):
    model = Profile
    ordering = ("effective_date",)
    extra = 0


@admin.register(Roster)
class RosterAdmin(admin.ModelAdmin):
    list_display = (
        "employee",
        "roster",
        "effective_date",
        "effective_to",
        "cycle_start",
        "rate_type",
        "repeating_unit",
    )
    list_filter = ("cycle_start", "rate_type")
    search_fields = (
        "roster__name",
        "employee__code",
        "employee__tax_number",
        "employee__first_name",
        "employee__last_name",
    )


class RosterInline(admin.TabularInline):
    model = Roster
    ordering = ("effective_date",)
    extra = 0


class AdditionalDateDetailInline(admin.TabularInline):
    model = AdditionalDateDetail
    ordering = ("effective_date",)
    extra = 0


class AdditionalNumberDetailInline(admin.TabularInline):
    model = AdditionalNumberDetail
    ordering = ("effective_date",)
    extra = 0


class AdditionalTextDetailInline(admin.TabularInline):
    model = AdditionalTextDetail
    ordering = ("effective_date",)
    extra = 0


@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("code", "tax_number")}),
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "preferred_name",
                    "middle_name",
                    "last_name",
                    "email",
                    "work_email",
                    "contact_number",
                    "address",
                    "date_of_birth",
                )
            },
        ),
        (
            "Employee info",
            {
                "fields": (
                    "date_of_hire",
                    "date_of_termination",
                    "is_active",
                ),
            },
        ),
    )
    list_display = (
        "code",
        "tax_number",
        "full_name",
        "short_name",
        "age",
        "tenure",
        "is_active",
    )
    list_filter = ("is_active",)
    search_fields = ("code", "tax_number", "first_name", "last_name")
    ordering = (
        "-is_active",
        "code",
    )

    inlines = (
        AdditionalDateDetailInline,
        AdditionalNumberDetailInline,
        AdditionalTextDetailInline,
        ProfileInline,
        RateInline,
        RosterInline,
    )
