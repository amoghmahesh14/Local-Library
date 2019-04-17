from django.contrib import admin

from .models import Author, Genre, Book, BookInstance

# Register your models here.


#admin.site.register(Book)
#admin.site.register(Author)
#admin.site.register(BookInstance)
admin.site.register(Genre)

#To display in inline the BookInstance along with it's Book detail
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

class BookInline(admin.TabularInline):
    model = Book

# Define the admin class
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]


# Register the admin class with the associated model

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	 list_display = ('title', 'author', 'display_genre') 
	 #Since genre is ManytoOne it should first be converted into a string ,Therefore display_genre function is called.
	 #This function is in catalog.models.py in Model of the Book.
	 inlines = [BooksInstanceInline] 	##To display in inline the BookInstance along with it's Book detail


  
   
# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

