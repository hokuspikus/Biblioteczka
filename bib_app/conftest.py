import pytest
from django.test import Client as WebClient
from django.contrib.auth.models import User
from bib_app.models import Author, Book

@pytest.fixture
def client():
    client = WebClient()
    return client


@pytest.fixture
def authors():
    lst = []
    a = Author.objects.create(first_name='costam', last_name='costam2')
    lst.append(a)
    b = Author.objects.create(first_name='costam2', last_name='costam3')
    lst.append(b)
    c = Author.objects.create(first_name='costam4', last_name='costam5')
    lst.append(c)
    return lst


@pytest.fixture
def author():
    a = Author.objects.create(first_name='cos', last_name='cos2')
    return a


@pytest.fixture
def book(author):
    b = Book.objects.create(title='costam', author=author)
    return b



@pytest.fixture
def user():
    user = User.objects.create_user(username='costam', password='costam77')
    return user