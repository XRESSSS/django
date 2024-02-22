from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Book


class BookListView(ListView):
    queryset = Book.objects.all()
    template_name = 'books/book_list.html'


def book_list(request):
    books = Book.object.all()

    context = {
        'book_list': books,
        'age': 55

    }
    return render(request, 'books/books/book_list.html', context)
