from django.contrib import admin

from notes.models import Note


# Register your models here.
@admin.register(Note)
class AdminNote(admin.ModelAdmin):
    ...
