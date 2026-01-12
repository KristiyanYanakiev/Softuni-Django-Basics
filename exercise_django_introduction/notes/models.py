from email.policy import default
from random import choices

from django.db import models

# Create your models here.
class Note(models.Model):

    class PriorityChoices(models.IntegerChoices):
        LOW = 1, 'Low'
        MEDIUM = 2, 'Medium'
        HIGH = 3, 'High'

    title = models.CharField(
        max_length=100
    )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    priority = models.IntegerField(
        choices=PriorityChoices.choices,
        default = PriorityChoices.LOW
    )
    category = models.ForeignKey(
        'categories.Category',
        on_delete=models.SET_NULL,
        related_name='notes',
        blank=True,
        null=True
    )

    def __str__(self):
       return self.title