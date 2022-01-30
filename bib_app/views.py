from django.shortcuts import render, redirect
# Create your views here.
from django.views import View

from bib_app.forms import AddPublisherForm, AddBookForm, CategoryForm
from bib_app.models import Author, Book, Publisher


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


class AddPublisherView(View):

    def get(self, request):
        form = AddPublisherForm()
        publishers = Publisher.objects.all()
        return render(request, 'addPublisher.html', {'form':form,'publishers':publishers})


    def post(self, request):
        form = AddPublisherForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            name = form.cleaned_data['name']
            Publisher.objects.create(name=name, year=year)
            #Publisher.objects.create(**form.cleaned_data)
            return redirect('books')
        return render(request, 'addPublisher.html', {'form': form})


class AddBookFormView(View):
    def get(self, request):
        form = AddBookForm()
        return render(request, 'addBookFrom.html', {'form':form})

    def post(self, request):
        form = AddBookForm(request.POST)
        if form.is_valid():
            Book.objects.create(**form.cleaned_data)
            return redirect('add_book_form_view')
        return render(request, 'addBookFrom.html', {'form': form})



class AddCategoryView(View):
    def get(self, request):
        form = CategoryForm()
        return render(request, 'addCategoryForm.html', {'form':form})

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            return redirect('add_category')
        return render(request, 'addCategoryForm.html', {'form': form})
