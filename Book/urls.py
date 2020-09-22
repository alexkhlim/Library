from django.urls import path
from Book.views import (books,
                        get_book,
                        create_book)

urlpatterns = [
    path('books/', books, name='main page'),
    path('books/<id>', get_book, name='book'),
    path('create/', create_book, name='page create')
]
