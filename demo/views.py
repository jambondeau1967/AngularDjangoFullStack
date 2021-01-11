from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book


class Another(View):

    books = Book.objects.all()
    #books = Book.objects.filter(is_published=True)
    # book = Book.objects.get(is_published=True) : just 1 record, for must be commented out.
    # book = Book.objects.get(id=1) : just 1 record, for must be commented out.
    lines = ''
    lines += f'We have {len(books)} books in database:<br>'
    lines += f'<br>'

    for book in books:
        thisbook = f'book: {book.title} with ID {book.id} in DB.<br>'
        lines += thisbook

    def get(self, request):
        return HttpResponse(self.lines)


def first(request):
    return HttpResponse('First message from views')
