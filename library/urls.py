from django.urls import path
from .apps import LibraryConfig
from .views import books_list, book_detail, BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

app_name = LibraryConfig.name

urlpatterns = [
    path('books_list/', books_list, name='books_list'),
    path('book_detail/<int:book_id>', book_detail, name='book_detail'),

    path('books/list/', BookListView.as_view(), name='book_new_list'),
    path('books/detail/<int:pk>/', BookDetailView.as_view(), name='book_new_detail'),
    path('books/create/', BookCreateView.as_view(), name='book_new_create'),
    path('books/update/<int:pk>', BookUpdateView.as_view(), name='book_new_update'),
    path('books/delete/<int:pk>', BookDeleteView.as_view(), name='book_new_delete'),

]
