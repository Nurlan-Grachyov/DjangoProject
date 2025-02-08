from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name="Фамилия")
    birth_date = models.DateField(verbose_name="Дата рождения")

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.birth_date} рождения'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['last_name']


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Книга')
    publication_date = models.DateField(verbose_name="Дата публикации")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f'{self.title} {self.author} {self.publication_date} выпуска'

    class Meta:
        verbose_name = 'Название книги'
        verbose_name_plural = 'Названия книг'
        ordering = ['title']
