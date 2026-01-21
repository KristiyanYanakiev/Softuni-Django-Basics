# populate_reviews.py

import os
import django
from random import choice, uniform
from datetime import datetime, timedelta

# Step 1: Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "exercise_templates.settings")
django.setup()

# Step 2: Import your models
from books.models import Book
from reviews.models import Review

# Step 3: List of sample authors and review texts
authors = [
    "Alice Johnson", "Bob Smith", "Charlie Brown", "Diana Prince",
    "Ethan Hunt", "Fiona Gallagher", "George Martin", "Hannah Baker",
    "Ian Fleming", "Julia Roberts"
]

sample_bodies = [
    "Absolutely loved this book! Highly recommended.",
    "Interesting read, but could have been shorter.",
    "I didn’t enjoy it as much as I expected.",
    "A masterpiece of storytelling and character development.",
    "Good book, but the ending was disappointing.",
    "This book changed my perspective on life.",
    "Well-written and engaging from start to finish.",
    "Not my favorite, but still worth reading.",
    "The plot was fantastic, I couldn’t put it down.",
    "Average book, some parts were boring."
]

# Step 4: Fetch all books
books = Book.objects.all()

# Step 5: Create 2 reviews per book
for book in books:
    for i in range(2):
        author = choice(authors)
        body = choice(sample_bodies)
        rating = round(uniform(2.0, 5.0), 2)  # random rating between 2.00 and 5.00

        review, created = Review.objects.get_or_create(
            author=author,
            book=book,
            defaults={
                "body": body,
                "rating": rating,
                "created_at": datetime.now() - timedelta(days=choice(range(365)))
            }
        )
        if created:
            print(f"Created review by {author} for {book.title}")
        else:
            print(f"Review by {author} for {book.title} already exists")

print("All reviews processed!")
