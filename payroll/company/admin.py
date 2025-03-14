from django.contrib import admin

from company.models import (
    Accumulator,
    AccumulatorMember,
    Allowance,
    AllowanceType,
    CustomBooleanField,
    CustomDateField,
    CustomNumberField,
    CustomTextField,
    Detail,
    RateType,
    RateTypeDefault,
)


class AccumulatorMemberInline(admin.TabularInline):
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


class AllowanceInline(admin.TabularInline):
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
        "unit_type",
    )
    list_filter = ("code",)
    search_fields = (
        "code",
        "description",
        "display_name",
    )
    ordering = ("code",)


@admin.register(CustomTextField)
class CustomTextFieldAdmin(admin.ModelAdmin):
    list_display = ("field_name",)
    list_filter = ("field_name",)
    search_fields = ("field_name",)
    ordering = ("field_name",)


@admin.register(CustomNumberField)
class CustomNumberFieldAdmin(admin.ModelAdmin):
    list_display = ("field_name",)
    list_filter = ("field_name",)
    search_fields = ("field_name",)
    ordering = ("field_name",)


@admin.register(CustomDateField)
class CustomDateFieldAdmin(admin.ModelAdmin):
    list_display = ("field_name",)
    list_filter = ("field_name",)
    search_fields = ("field_name",)
    ordering = ("field_name",)


@admin.register(CustomBooleanField)
class CustomBooleanFieldAdmin(admin.ModelAdmin):
    list_display = ("field_name",)
    list_filter = ("field_name",)
    search_fields = ("field_name",)
    ordering = ("field_name",)


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


class RateTypeDefaultInline(admin.TabularInline):
    model = RateTypeDefault
    extra = 0


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
    inlines = (RateTypeDefaultInline,)
