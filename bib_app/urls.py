"""biblioteka2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from bib_app import views

urlpatterns = [
    path('authors/', views.AuthorView.as_view(), name='authors'),
    path('add_author/', views.AddAuthor.as_view(), name='add_authors'),
    path('add_book/', views.AddBook.as_view(), name='add_book'),
    path('books/', views.BooksView.as_view(), name='books'),
    path('add_publisher/', views.AddPublisherView.as_view(), name='add_publisher'),
    path('add_book_form/', views.AddBookFormView.as_view(), name='add_book_form_view'),
    path('add_book_by_create_view/', views.CreateBookView.as_view(), name='add_book_by_create_view'),
    path('add_category_form/', views.AddCategoryView.as_view(), name='add_category'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail_view'),
]
