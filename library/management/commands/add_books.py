from django.core.management.base import BaseCommand
from library.models import Author, Book


class Command(BaseCommand):
    help = 'Add test books to the database'

    def handle(self, *args, **kwargs):
        author, unknown = Author.objects.get_or_create(first_name='Anton', last_name='Chehov', birth_date='1860-01-29')

        books = [
            {'title': 'Вишневый сад', 'publication_date': '1904-01-01', 'author': author},
            {'title': 'Три сестры', 'publication_date': '1901-01-01', 'author': author},
        ]

        for book_data in books:
            book, created = Book.objects.get_or_create(**book_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added book: {book.title}'))
            else:
                self.stdout.write(self.style.warning(f'Book already exists: {book.title}'))
