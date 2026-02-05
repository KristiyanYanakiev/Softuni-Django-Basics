from email.policy import default

from django import forms
from django.core.exceptions import ValidationError

from books.models import Book, Tag


class BookFormBasic(forms.ModelForm):
    PAYMENT_CHOICES = (
        ('Card', 'Card'),
        ('Cash', 'Cash')
    )
    tags = forms.ModelChoiceField(
        queryset=Tag.objects.all(),
        empty_label='Please select a tag',
        required=False

    )
    payment_method = forms.ChoiceField(
        choices=PAYMENT_CHOICES
    )
    class Meta:
        model = Book
        exclude = ['slug']
        error_messages = {
            'title': {
                'unique': "Title is not unique. Please enter another one"
            }
        }

    def clean_isbn(self):

        if self.cleaned_data['isbn'].startswith('987'):
            raise ValidationError('ISBN cannot start with 987')

        return self.cleaned_data['isbn']

    def clean(self) -> dict:
        cleaned = super().clean()

        genre = cleaned.get('genre')
        price = cleaned.get('price')

        if genre == 'Fiction' and price < 10:
            raise ValidationError('Books of type Fiction cannot have a price less than 10')

        return cleaned

    def save(self, commit=True):
        instance = super().save(commit=False)

        if instance.title:
            instance.title = instance.title.capitalize()

        if commit:
            instance.save()

        return instance








class BookCreateForm(BookFormBasic):
    ...

class BookEditForm(BookFormBasic):
    ...

class BookSearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        required=False
    )

