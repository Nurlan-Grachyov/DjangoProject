from django.urls import path
from .apps import LibraryConfig
from .views import books_list, book_detail

app_name = LibraryConfig.name

urlpatterns = [
    path('books_list/', books_list, name='books_list'),
    path('book_detail/<int:book_id>', book_detail, name='book_detail'),
]
