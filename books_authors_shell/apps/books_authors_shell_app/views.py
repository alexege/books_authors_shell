from django.shortcuts import render, HttpResponse, redirect
from .models import Book
from .models import Author
from . import models

#Landing page
def index(request):
    context = {
        'books' : models.Book.objects.all(),
        'authors' : models.Author.objects.all()
    }

    return render(request, "books_authors_shell_app/index.html", context)

#Route for localhost:8000/books/4 - Pulls book information with id from database
def book_description(request, id):
    context = {
        'books' : models.Book.objects.all(),
        'book' : models.Book.objects.get(id=id),
        'authors' : models.Author.objects.all(),
        'author_list' : models.Book.objects.get(id=id).Author.all(),
    }
    return render(request, "books_authors_shell_app/books.html", context, id)

#Route for localhost:8000/add_book - Adds a book to the database
def add_book(request):
    context = {
        'books' : models.Book.objects.all(),
        'authors' : models.Author.objects.all()
    }
    models.Book.objects.create(title=request.POST['title'], desc=request.POST['description'])
    return redirect('/')

#Route for localhost:8000/authors - Render Authors page
def authors(request):
    context = {
        'authors' : models.Author.objects.all(),
    }
    return render(request, "books_authors_shell_app/authors.html", context)

#Route for localhost:8000/add_author
def add_author(request):
    book_id = request.POST['book_id']
    author_id = request.POST['author_id']
    models.Book.objects.get(id=book_id).Author.add(Author.objects.get(id=author_id))
    return redirect('/')

#Route for localhost:8000/authors/4
def create_author(request):
    models.Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
    return redirect('/authors')
    # return render(request, "books_authors_shell_app/authors.html")

#Render details page about "viewed" author
def author_description(request, id):
    context = {
        'author' : models.Author.objects.get(id=id),
        'book_list' : models.Author.objects.get(id=id).books.all(),
        'all_books' : models.Book.objects.all(),
    }
    return render(request, "books_authors_shell_app/author.html", context, id)

#Add an author to the list of authors for given book
def add_author_to_book(request):
    book_id = request.POST['book_id']
    author_id = request.POST['author_id']
    models.Author.objects.get(id=author_id).books.add(Book.objects.get(id=book_id))
    return redirect('/authors')