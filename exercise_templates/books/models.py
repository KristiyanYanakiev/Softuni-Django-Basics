from django.db import models
from django.utils.text import slugify

from books.validators import RangeValidator


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
    price = models.DecimalField(max_digits=6, decimal_places=2,  validators=[RangeValidator(0, 1000, message='Price should be in the range 0 - 1000')])
    isbn = models.CharField(max_length=12, unique=False)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    publishing_date = models.DateField()
    description = models.TextField()
    image_url = models.URLField()
    cover_img = models.ImageField(blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    # tags = models.ManyToManyField('Tag') Why it does not work without this line?



    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(
        max_length=50,
    )

    books = models.ManyToManyField(
        to='Book'
    )

    def __str__(self) -> str:
        return self.name