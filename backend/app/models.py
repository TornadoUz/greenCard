from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class GenderChoices(models.TextChoices):
    MALE = "male"
    FEMALE = "female"


class MaritalStatusChoices(models.TextChoices):
    SINGLE = "single"
    MARRIED = "married"
    DIVORCED = "divorces"
    WIDOWED = "widowed"


class BotUser(models.Model):
    telegram_id = models.CharField(
        max_length=30,
        unique=True,
        verbose_name="Telegram ID",
    )

    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "bot_users"
        verbose_name = "Bot user"
        verbose_name_plural = "Bot users"


class Season(models.Model):
    year = models.PositiveSmallIntegerField(unique=True)

    class Meta:
        db_table = "seasons"
        verbose_name = "Season"
        verbose_name_plural = "Seasons"


class Application(models.Model):
    bot_user = models.ForeignKey(
        BotUser, on_delete=models.CASCADE, verbose_name="Bot user"
    )
    season = models.ForeignKey(Season, on_delete=models.CASCADE, verbose_name="Season")

    phone_number = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name="Phone Number",
    )
    first_name = models.CharField(
        max_length=150, null=True, blank=True, verbose_name="First name"
    )
    last_name = models.CharField(
        max_length=150, null=True, blank=True, verbose_name="First name"
    )
    gender = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        choices=GenderChoices.choices,
        verbose_name="Gender",
    )
    birth_date = models.DateField(null=True, blank=True, verbose_name="Birth date")
    birth_country = models.CharField(
        max_length=150, null=True, blank=True, verbose_name="Birth country"
    )
    birth_city = models.CharField(
        max_length=150, null=True, blank=True, verbose_name="Birth city"
    )
    nationality = models.CharField(
        max_length=150, null=True, blank=True, verbose_name="Nationality"
    )
    passport_number = models.CharField(
        max_length=150, null=True, blank=True, verbose_name="Passport number"
    )
    passport_exp_date = models.DateField(
        null=True, blank=True, verbose_name="Passport expiration date"
    )
    email = models.EmailField(
        max_length=255, null=True, blank=True, verbose_name="Email"
    )
    marital_status = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        choices=MaritalStatusChoices.choices,
        verbose_name="Marital status",
    )
    children_count = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name="Children count"
    )

    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "applications"
        unique_together = (
            "bot_user",
            "season",
        )
        verbose_name = "Application"
        verbose_name_plural = "Applications"
