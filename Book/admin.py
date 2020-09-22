from django.contrib import admin
from Book.models import Book


class BookAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'author', 'author_name')
    search_fields = 'title',
    list_display = 'title', 'short_description', 'author'
    list_filter = 'author',


admin.site.register(Book, BookAdmin)
