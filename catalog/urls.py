from django.contrib import admin
from django.urls import path
from . import views
from catalog.views import BookListView 



app_name = 'catalog'

urlpatterns = [

	#/catalog/
    path('', views.index , name='index'),

    #/catalog/books/
    #path('books/',views.books , name='books'),
    path('books/', BookListView.as_view(), name='books'),

    #/catalog/books/book_id
    path('book/<int:book_id>', views.BookDetail, name='book_detail'),

    #/catalog/authors/
    path('authors/',views.authors , name='authors'),

    #/catalog/authors/author_id
    path('author/<int:author_id>', views.AuthorDetail, name='author_detail'),



    
]
	