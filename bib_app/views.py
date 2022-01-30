from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView

from bib_app.forms import AddPublisherForm, AddBookForm, CategoryForm, BookModelForm
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
        form = BookModelForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = BookModelForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('books')
        return render(request, 'form.html', {'form': form})

class BooksView(View):
    def get(self, request):
        books= Book.objects.all()
        return render(request, 'books.html',  {'books':books})


class AddPublisherView(View):

    def get(self, request):
        form = AddPublisherForm()
        publishers = Publisher.objects.all()
        return render(request, 'form.html', {'form':form,'publishers':publishers})


    def post(self, request):
        form = AddPublisherForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            name = form.cleaned_data['name']
            Publisher.objects.create(name=name, year=year)
            #Publisher.objects.create(**form.cleaned_data)
            return redirect('books')
        return render(request, 'form.html', {'form': form})


class AddBookFormView(View):
    def get(self, request):
        form = AddBookForm()
        return render(request, 'form.html', {'form':form})

    def post(self, request):
        form = AddBookForm(request.POST)
        if form.is_valid():
            Book.objects.create(**form.cleaned_data)
            return redirect('add_book_form_view')
        return render(request, 'form.html', {'form': form})



class AddCategoryView(View):
    def get(self, request):
        form = CategoryForm()
        return render(request, 'form.html', {'form':form})

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            return redirect('add_category')
        return render(request, 'form.html', {'form': form})


class CreateBookView(CreateView):
    model = Book
    form_class = BookModelForm
    template_name = 'form.html'
    success_url = reverse_lazy('books') # '/books/'

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail_view.html'
