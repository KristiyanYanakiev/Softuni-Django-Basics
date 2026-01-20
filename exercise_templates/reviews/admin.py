from django.contrib import admin

from reviews.models import Review


# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("author", "book", "rating", "created_at")
    search_fields = ("author", "book__title")
    list_filter = ("rating", "created_at")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)