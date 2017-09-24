from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book


# def search_form(request):
#     return render(request, 'search_form.html')


def search(request):
    errors = []
    if 'q' in request.GET:
        # message = 'You searched for: %r' % request.GET['q']
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html', {
                'books': books,
                'query': q
            })
        # message = 'You submitted an empty form.'
        # return HttpResponse('Please submit a search term.')
    # return HttpResponse(message)
    return render(request, 'search_form.html', {'errors': errors})