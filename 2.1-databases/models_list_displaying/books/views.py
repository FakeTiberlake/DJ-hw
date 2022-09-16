from django.shortcuts import render

from books.models import Book


def books_view(request, date=None):
    template = 'books/books_list.html'
    context = {}

    if date:
        books = Book.objects.filter(pub_date=date)
        books_previous = Book.objects.filter(pub_date__lt=date).order_by('-pub_date').first()
        books_next = Book.objects.filter(pub_date__gt=date).order_by('pub_date').first()

        if books_previous:
            books_previous.pub_date = str(books_previous.pub_date)
            context['books_previous'] = books_previous
        if books_next:
            books_next.pub_date = str(books_next.pub_date)
            context['books_next'] = books_next

    else:
        books = Book.objects.all()

    for book in books:
        book.pub_date = str(book.pub_date)
    context['books'] = books

    return render(request, template, context)




