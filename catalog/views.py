from django.shortcuts import render
from django.views import generic
from .models import Author, Book, BookInstance, Genre


def index(request):
    """
    View function for the homepage
    """
    context = {
        'number_of_books': Book.objects.all().count(),
        'number_of_book_instances': BookInstance.objects.all().count(),
        'number_of_available_book_instances':
            BookInstance.objects.filter(status__exact='a').count(),
        'number_of_authors': Author.objects.count(),
        'title': 'Local Library Home',
        'number_of_books_with_title_containing_elon':
            Book.objects.filter(title__icontains='elon').count(),
        'number_of_genres_whose_name_contains_phy':
            Genre.objects.filter(name__icontains='phy').count(),
    }

    return render(
        request,
        'index.html',
        context=context
    )


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 2


class AuthorDetailView(generic.DetailView):
    model = Author


class BookListView(generic.ListView):
    model = Book
    paginate_by = 2


class BookDetailView(generic.DetailView):
    model = Book
