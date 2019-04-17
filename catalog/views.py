from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from catalog.models import Book, Author, BookInstance, Genre
from django.views.generic.list import ListView 

# Create your views here.

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'catalog/index.html', context=context)
	


"""def books(request):
	all_books = Book.objects.all()
	context = {'all_books':all_books}

	return render(request,'catalog/books.html',context )"""

class BookListView(ListView):
	template_name = 'catalog/books.html'
	queryset = Book.objects.all()
	context_object_name = 'all_books'
	paginate_by = 10


def BookDetail(request , book_id):
	book = get_object_or_404(Book,pk=book_id)
	
	return render(request ,'catalog/book_detail.html',{ 'book' : book})

def AuthorDetail(request , author_id):
	author = get_object_or_404(Author,pk=author_id)
	
	return render(request ,'catalog/author_detail.html',{ 'author' : author})





def authors(request):
	all_authors = Author.objects.all()
	context = {'all_authors':all_authors}

	return render(request,'catalog/authors.html',context )

