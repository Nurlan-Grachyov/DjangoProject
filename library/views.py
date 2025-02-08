from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from library.models import Book


def books_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'library/books_list.html', context)

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {'book': book}
    return render(request, 'library/book_detail.html', context)

class BookListView(ListView):
    model = Book
    template_name = "library/book_new_list.html"
    context_object_name = 'books'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(publication_date__year__gt = 2000)


class BookDetailView(DetailView):
    model = Book
    template_name = "library/book_new_detail.html"
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count_books'] = Book.objects.filter(author=self.object.author).count()
        return context


class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'publication_date']
    template_name = "library/book_new_create.html"
    context_object_name = 'book'
    success_url = reverse_lazy('library:book_new_list')

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'publication_date']
    template_name = "library/book_new_create.html"
    context_object_name = 'book'
    success_url = reverse_lazy('library:book_new_list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = "library/book_new_delete.html"
    context_object_name = 'book'
    success_url = reverse_lazy('library:book_new_list')