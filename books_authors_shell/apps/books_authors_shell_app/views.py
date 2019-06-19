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

#Route for localhost:8000/books
# def books(request):
#     pass
#     return render(request, "books_authors_shell_app/books.html")

#
def add_book(request):
    context = {
        'books' : models.Book.objects.all(),
        'authors' : models.Author.objects.all()
    }
    models.Book.objects.create(title=request.POST['title'], desc=request.POST['description'])
    return redirect('/')

#Route for localhost:8000/add_author
def add_author(request):
    book_id = request.POST['book_id']
    author_id = request.POST['author_id']
    models.Book.objects.get(id=book_id).Author.add(Author.objects.get(id=author_id))

    return redirect('/')

#Route for localhost:8000/authors
def authors(request):
    context = {
        'authors' : models.Author.objects.all(),
    }
    return render(request, "books_authors_shell_app/authors.html", context)



#Route for localhost:8000/authors/4
def authors_id(request):
    models.Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
    return redirect('/authors')
    # return render(request, "books_authors_shell_app/authors.html")

#Route for localhost:8000/books/4
def books_id(request, id):
    context = {
        'books' : models.Book.objects.all(),
        'book' : models.Book.objects.get(id=id),
        'authors' : models.Author.objects.all(),
        'author_list' : models.Book.objects.get(id=id).Author.all(),
    }

    # print(context['books'])

    return render(request, "books_authors_shell_app/books.html", context, id)