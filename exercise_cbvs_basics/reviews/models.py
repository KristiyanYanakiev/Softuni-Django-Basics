from django.core.exceptions import ValidationError
from django.db import models

from destinations.models import Destination
from travelers.models import Traveler


# Create your models here.
class Review(models.Model):
    REVIEW_TYPE_CHOICES = [
        ("TEXT", "Text"),
        ("VIDEO", "Video"),
        ("AUDIO", "Audio"),
    ]

    body = models.TextField()
    rating = models.DecimalField(max_digits=4, decimal_places=2)
    is_verified = models.BooleanField(default=False)
    review_type = models.CharField(max_length=10, choices=REVIEW_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    # Relations
    traveler = models.ForeignKey(Traveler, on_delete=models.CASCADE, related_name="reviews")
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name="reviews")

    # Extra fields
    title = models.CharField(max_length=150, blank=True)

    def clean(self):
        # Rating validation
        if not (0 <= self.rating <= 5):
            raise ValidationError("Rating must be between 0.00 and 5.00.")

        # Prevent review if destination unavailable
        if not self.destination.is_available:
            raise ValidationError("Cannot review an unavailable destination.")

    def __str__(self):
        return f"Review by {self.traveler} for {self.destination}"