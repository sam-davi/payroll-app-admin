from django.db import models


class Frequency(models.IntegerChoices):
    WEEKLY = 52, "Weekly"
    FORTNIGHTLY = 26, "Fortnightly"
    FOURWEEKLY = 13, "Fourweekly"
    MONTHLY = 12, "Monthly"
    QUARTERLY = 4, "Quarterly"
    ANNUAL = 1, "Annual"
    MANUAL = 0, "Manual"


class UnitTypes(models.IntegerChoices):
    HOURLY = 2080, "Hourly"
    DAILY = 260, "Daily"
    WEEKLY = 52, "Weekly"
    FORTNIGHTLY = 26, "Fortnightly"
    FOURWEEKLY = 13, "Fourweekly"
    MONTHLY = 12, "Monthly"
    ANNUAL = 1, "Annual"


class ConversionMethods(models.IntegerChoices):
    WEEKS = 364, "52 Weeks per Year"
    DAYS = 365, "365 Days per Year"
