from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify

from travelers.models import Traveler


# Create your models here.
class Destination(models.Model):
    COUNTRY_CHOICES = Traveler.COUNTRY_CHOICES

    name = models.CharField(max_length=150)
    country = models.CharField(max_length=10, choices=COUNTRY_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Relations
    travelers = models.ManyToManyField(Traveler, related_name="destinations", blank=True)

    # Extra fields
    created_at = models.DateTimeField(auto_now_add=True)
    duration_days = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ("name", "country")

    def clean(self):
        # Price validation
        if self.price < 0:
            raise ValidationError("Price cannot be negative.")

        # Unique combination validation (extra safety)
        if Destination.objects.exclude(pk=self.pk).filter(
            name=self.name,
            country=self.country
        ).exists():
            raise ValidationError("Destination with this name and country already exists.")

    def save(self, *args, **kwargs):
        # Auto-generate slug
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.country})"
