from django.contrib import admin
from django.db.models import Count
from .models import Author, Book


class BookInline(admin.TabularInline):
    model = Book


@admin.register(Author)
class Name_author(admin.ModelAdmin):
    list_display = ('last_name', 'books')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(books=Count('book'))
        return queryset

    @staticmethod
    @admin.display(description='Количество книг')
    def books(obj):
        return obj.books

    inlines = [
        BookInline,
    ]


@admin.register(Book)
class Name_book(admin.ModelAdmin):
    list_display = ('title', 'author',)
