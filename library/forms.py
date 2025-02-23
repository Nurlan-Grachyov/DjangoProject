from xml.dom import ValidationErr

from django import forms
from django.core.exceptions import ValidationError

from .models import Book, Author


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'publication_date', 'author', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название'
        })

        self.fields['publication_date'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите дату публикации',
            'type': 'date'
        })

        self.fields['author'].widget.attrs.update({
            'class': 'form-control',
        })

    def clean(self):
        title = self.cleaned_data.get('title')
        author = self.cleaned_data.get('author')

        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError('A book with this author and title already exists')



class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'birth_date', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите имя'
        })

        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите фамилию'
        })

        self.fields['birth_date'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите дату рождения',
            'type': 'date'
        })

    def clean(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        if Author.objects.filter(first_name=first_name, last_name=last_name).exists():
            raise ValidationError('An author with this first name and last name already exists')
