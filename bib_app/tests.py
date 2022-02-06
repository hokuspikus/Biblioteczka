from urllib import request

from django.urls import reverse
import pytest
from bib_app.models import Author, Book


def test_index(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_authors(client, authors):
    url = reverse('authors')
    response = client.get(url)
    assert response.status_code == 200
    context = response.context
    assert context['authors'].count() == len(authors)
    for item in authors:
        assert item in context['authors']


@pytest.mark.django_db
def test_add_author(client):
    dct = {
        'first_name': 'costam',
        'last_name': 'costam2'
    }
    url = reverse('add_authors')
    client.post(url, dct)
    assert Author.objects.get(**dct)


@pytest.mark.django_db
def test_add_book(client, author):
    dct = {
        'title': 'costam',
        'author': author.id
    }
    url = reverse('add_book')
    client.post(url, dct)
    assert Book.objects.first()


@pytest.mark.django_db
def test_login(client, user):
    dct = {
        'username': 'costam',
        'password': 'costam77'
    }
    url = reverse('login')
    response = client.post(url, dct)
    assert response.wsgi_request.user.is_authenticated


@pytest.mark.django_db
def test_publisher_add_view_without_login(client):
    url = reverse('add_publisher')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_publisher_add_view_with_login(user, client):
    url = reverse('add_publisher')
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200
