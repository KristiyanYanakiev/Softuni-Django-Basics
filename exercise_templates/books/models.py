from django.db import models
from django.utils.text import slugify



class Book(models.Model):
    GENRE_CHOICES = [
        ("Fiction", "Fiction"),
        ("Non-Fiction", "Non-Fiction"),
        ("Fantasy", "Fantasy"),
        ("Science", "Science"),
        ("Biography", "Biography"),
        ("History", "History"),

    ]

    title = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    isbn = models.CharField(max_length=12, unique=True)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    publishing_date = models.DateField()
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title