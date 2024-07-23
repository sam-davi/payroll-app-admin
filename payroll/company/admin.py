from django.contrib import admin

from .models import (
    Accumulator,
    AccumulatorMember,
    Allowance,
    AllowanceType,
    Detail,
    RateType,
)


class AccumulatorMemberInline(admin.StackedInline):
    model = AccumulatorMember
    extra = 0


@admin.register(Accumulator)
class AccumulatorAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "description",
        "field_type",
    )
    list_filter = ("code",)
    search_fields = (
        "code",
        "description",
    )
    ordering = ("code",)

    inlines = (AccumulatorMemberInline,)


class AllowanceInline(admin.StackedInline):
    model = Allowance
    extra = 0


@admin.register(AllowanceType)
class AllowanceTypeAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "description",
    )
    list_filter = ("code",)
    search_fields = (
        "code",
        "description",
    )
    exclude = ("accumulators",)
    ordering = ("code",)

    inlines = (
        AccumulatorMemberInline,
        AllowanceInline,
    )


@admin.register(Allowance)
class AllowanceAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "description",
        "display_name",
        "allowance_type",
    )
    list_filter = ("code",)
    search_fields = (
        "code",
        "description",
        "display_name",
    )
    ordering = ("code",)


# Register your models here.
@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "name",
        "tax_number",
        "address",
        "email",
        "contact_number",
    )
    list_filter = ("code",)
    search_fields = (
        "code",
        "name",
        "tax_number",
        "address",
        "email",
        "contact_number",
    )
    ordering = ("code",)


@admin.register(RateType)
class RateTypeAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "description",
    )
    list_filter = ("code",)
    search_fields = (
        "code",
        "description",
    )
    ordering = ("code",)
