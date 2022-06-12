from django.db import models


class Author(models.Model):
    first_name = models.CharField('Имя автора', max_length=50)
    last_name = models.CharField('Фамилия автора', max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField('Название книги', max_length=100)
    pub_date = models.DateField('Дата публикации')
    pages = models.IntegerField('Количество страниц')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

