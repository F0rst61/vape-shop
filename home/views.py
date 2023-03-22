from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view that returns the index page """

    return render(request, 'home/index.html')
