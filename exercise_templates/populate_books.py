# populate_books.py

import os
import django
from datetime import date

# Step 1: Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "exercise_templates.settings")
django.setup()

# Step 2: Import your model
from books.models import Book

# Step 3: List of books
books_data = [
    {
        "title": "To Kill a Mockingbird",
        "price": 15.99,
        "isbn": "223456789012",
        "genre": "Fiction",
        "publishing_date": date(1960, 7, 11),
        "description": "A novel by Harper Lee about racial injustice and moral growth in the American South.",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/7/79/To_Kill_a_Mockingbird.JPG",
    },
    {
        "title": "Sapiens",
        "price": 22.50,
        "isbn": "223456789013",
        "genre": "Non-Fiction",
        "publishing_date": date(2011, 1, 1),
        "description": "Yuval Noah Harari explores the history and impact of Homo sapiens.",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/7/7d/Sapiens_book_cover.jpg",
    },
    {
        "title": "Dune",
        "price": 18.75,
        "isbn": "223456789014",
        "genre": "Fantasy",
        "publishing_date": date(1965, 8, 1),
        "description": "Frank Herbert’s epic science fantasy novel set on the desert planet Arrakis.",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/a/a5/Dune_First_Edition.jpg",
    },
    {
        "title": "A Brief History of Time",
        "price": 21.00,
        "isbn": "223456789015",
        "genre": "Science",
        "publishing_date": date(1988, 4, 1),
        "description": "Stephen Hawking explains cosmology for the general public.",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/b/bb/BriefHistoryTime.jpg",
    },
    {
        "title": "The Catcher in the Rye",
        "price": 13.99,
        "isbn": "223456789016",
        "genre": "Fiction",
        "publishing_date": date(1951, 7, 16),
        "description": "A novel by J.D. Salinger exploring teenage alienation.",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/3/32/Rye_catcher.jpg",
    },
    {
        "title": "Steve Jobs",
        "price": 20.00,
        "isbn": "223456789017",
        "genre": "Biography",
        "publishing_date": date(2011, 10, 24),
        "description": "The authorized biography of Apple co-founder Steve Jobs by Walter Isaacson.",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/e/e4/Steve_Jobs_by_Walter_Isaacson.jpg",
    },
    {
        "title": "Guns, Germs, and Steel",
        "price": 19.25,
        "isbn": "223456789018",
        "genre": "History",
        "publishing_date": date(1997, 3, 1),
        "description": "Jared Diamond examines the factors shaping human societies.",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/9/9b/Ggs_book_cover.jpg",
    },
    {
        "title": "The Name of the Wind",
        "price": 16.80,
        "isbn": "223456789019",
        "genre": "Fantasy",
        "publishing_date": date(2007, 3, 27),
        "description": "The first book of The Kingkiller Chronicle by Patrick Rothfuss.",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/6/6b/TheNameOfTheWind_cover.jpg",
    },
    {
        "title": "Thinking, Fast and Slow",
        "price": 17.90,
        "isbn": "223456789020",
        "genre": "Non-Fiction",
        "publishing_date": date(2011, 10, 25),
        "description": "Daniel Kahneman explores the two systems that drive human thinking.",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/c/c1/Thinking%2C_Fast_and_Slow.jpg",
    },
    {
        "title": "The Great Gatsby",
        "price": 12.99,
        "isbn": "223456789021",
        "genre": "Fiction",
        "publishing_date": date(1925, 4, 10),
        "description": "F. Scott Fitzgerald’s novel of the Jazz Age and the American Dream.",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/f/f7/TheGreatGatsby_1925jacket.jpeg",
    },
]

# Step 4: Create the books
for book_data in books_data:
    book, created = Book.objects.get_or_create(
        title=book_data["title"],
        defaults=book_data
    )
    if created:
        print(f"Created: {book.title}")
    else:
        print(f"Already exists: {book.title}")

print("All books processed!")
