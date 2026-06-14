from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
class Traveler(models.Model):
    COUNTRY_CHOICES = [
        ("BG", "Bulgaria"),
        ("UK", "United Kingdom"),
        ("DE", "Germany"),
        ("FR", "France"),
        ("ES", "Spain"),
        ("IT", "Italy"),
        ("US", "United States"),
        ("OTHER", "Other"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    country = models.CharField(max_length=10, choices=COUNTRY_CHOICES)
    registered_at = models.DateTimeField(auto_now_add=True)

    # Extra fields
    bio = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    view_count = models.PositiveIntegerField()

    def clean(self):
        # Age validation
        if self.age < 18:
            raise ValidationError("Traveler must be at least 18 years old.")

        # Email domain validation
        allowed_domains = ["university.com", "university.org"]
        domain = self.email.split("@")[-1]
        if domain not in allowed_domains:
            raise ValidationError("Email must be from university.com or university.org.")

    def __str__(self):
        return f"{self.name} ({self.email})"