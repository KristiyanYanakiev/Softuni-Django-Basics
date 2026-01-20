from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "isbn", "genre", "price", "publishing_date", "updated_at")
    search_fields = ("title", "isbn", "genre")
    list_filter = ("genre", "publishing_date")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("-publishing_date",)
    readonly_fields = ("updated_at",)


