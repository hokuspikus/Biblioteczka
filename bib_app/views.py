from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from bib_app.models import Author, Book


class Index(View):
    def get(self, request):
        return render(request, 'base.html')


class AuthorView(View):
    def get(self, request):
        a = Author.objects.all()
        return render(request, 'authors.html', {'authors': a})


class AddAuthor(View):
    def get(self, request):
        return render(request, 'add_author.html', )

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        Author.objects.create(first_name=first_name, last_name=last_name)
        return redirect('authors')


class AddBook(View):
    def get(self, request):
        authors = Author.objects.all()
        return render(request, 'add_book.html', {'authors': authors})

    def post(self, request):
        title = request.POST.get('title')
        author_id = request.POST.get('author_id')
        author = Author.objects.get(id=author_id)
        Book.objects.create(title=title, author=author)
        return redirect('books')

class BooksView(View):
    def get(self, request):
        books= Book.objects.all()
        return render(request, 'books.html',  {'books':books})