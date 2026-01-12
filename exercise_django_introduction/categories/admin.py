from django.contrib import admin

# Register your models here.
from django.contrib import admin

from categories.models import Category


# Register your models here.
@admin.register(Category)
class AdminNote(admin.ModelAdmin):
    ...
