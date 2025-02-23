from django.urls import path
from .apps import LibraryConfig
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, \
    BookDeleteView, AuthorCreateView, AuthorUpdateView, AuthorListView, RecommendBookView, ReviewBookView

app_name = LibraryConfig.name

urlpatterns = [
    path('books/list/', BookListView.as_view(), name='book_new_list'),
    path('books/detail/<int:pk>/', BookDetailView.as_view(), name='book_new_detail'),
    path('books/create/', BookCreateView.as_view(), name='book_new_create'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book_new_update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book_new_delete'),
    path('books/review/<int:book_id>/', ReviewBookView.as_view(), name='review_book'),
    path('books/recommend/<int:book_id>/', RecommendBookView.as_view(), name='recommend_book'),

    path('author/create/', AuthorCreateView.as_view(), name='author_create'),
    path('author/update/<int:pk>/', AuthorUpdateView.as_view(), name='author_update'),
    path('author/list/', AuthorListView.as_view(), name='author_list'),

]
