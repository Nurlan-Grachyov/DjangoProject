from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.cache import cache
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from library.forms import BookForm, AuthorForm
from library.models import Book, Author
from library.services import ServicesReview


class ReviewBookView(LoginRequiredMixin, View):
    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)

        if not request.user.has_perm('can_review_book'):
            return HttpResponseForbidden('У вас нет прав рецензировать')

        book.review = request.POST.get('review')
        book.save()
        return redirect('library:book_new_detail', id=book_id)


class RecommendBookView(LoginRequiredMixin, View):
    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)

        if not request.user.has_perm('can_recommend_book'):
            return HttpResponseForbidden('У вас нет прав рекомендовать')

        book.recommended = True
        book.save()
        return redirect('library:book_new_detail', id=book_id)


class AuthorCreateView(LoginRequiredMixin, CreateView):
    model = Author
    template_name = 'library/author/author_create.html'
    form_class = AuthorForm
    success_url = reverse_lazy('library:author_list')


class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    model = Author
    template_name = 'library/author/author_create.html'
    form_class = AuthorForm
    success_url = reverse_lazy('library:author_list')


class AuthorListView(ListView):
    model = Author
    template_name = "library/author/author_list.html"
    context_object_name = 'authors'

    def get_queryset(self):
        queryset = cache.get('authors_queryset')
        if not queryset:
            queryset = super().get_queryset()
            cache.set('authors_queryset', queryset, 60 * 15)
        return queryset


@method_decorator(cache_page(60 * 15), name='dispatch')
class BookListView(ListView):
    model = Book
    template_name = "library/book/book_list.html"
    context_object_name = 'books'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(publication_date__year__gt=1900)


@method_decorator(cache_page(60 * 15), name='dispatch')
class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    template_name = "library/book/book_detail.html"
    context_object_name = 'book'
    permission_required = 'library.view_book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_id = self.object.id
        context['count_books'] = Book.objects.filter(author=self.object.author).count()
        context['average_rating'] = ServicesReview.calculate_average_rating(book_id)
        context['is_popular'] = ServicesReview.is_popular(book_id)
        return context


class BookCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = "library/book/book_create.html"
    success_url = reverse_lazy('library:book_new_list')
    permission_required = 'library.add_book'


class BookUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = "library/book/book_create.html"
    context_object_name = 'book'
    success_url = reverse_lazy('library:book_new_list')
    permission_required = 'library.change_book'


class BookDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = "library/book/book_delete.html"
    context_object_name = 'book'
    success_url = reverse_lazy('library:book_new_list')
    permission_required = 'library.delete_book'
