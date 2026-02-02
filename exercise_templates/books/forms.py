from email.policy import default

from django import forms

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
        exclude = ['slug', 'isbn']


class BookCreateForm(BookFormBasic):
    ...

class BookEditForm(BookFormBasic):
    ...

class BookSearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        required=False
    )