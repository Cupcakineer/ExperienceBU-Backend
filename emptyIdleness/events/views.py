from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [ # list of dictionaries

    {
        'author': 'Ryan Li',
        'title': 'Event 1',
        'content': 'Event 1 Content',
        'date_uploaded': 'March 24, 2020'
    },
    {
        'author': 'Tung Truong',
        'title': 'Event 2',
        'content': 'Event 2 Content',
        'date_uploaded': 'March 25, 2020'
    }


]


def index(request):
    context = {'posts': posts}
    #return HttpResponse("<h1>This is the events homepage <h1>")
    return render(request, 'events/index.html', context)

def about(request):

    #return HttpResponse("<h1>About Page<h1>")
    return render(request, 'events/about.html', {'title': 'About Page'})