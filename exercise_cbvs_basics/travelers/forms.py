from django import forms

from reviews.models import Traveler


class TravelerForm(forms.ModelForm):
    class Meta:
        model = Traveler
        exclude = ['created_at']

        error_messages = {
            "age": {
                "min_value": "A traveler must be at least 18 years old",
            },
            "email": {
                "invalid": "Provide a valid university email address",
            },
        }
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Joe Doe"}),
            "email": forms.EmailInput(attrs={"placeholder": "student@university.com/student@university.org"})
        }