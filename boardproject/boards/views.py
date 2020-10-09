from django.shortcuts import render
from django.http import Http404
from .models import Board


def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})


def about(request):
    return render(request, 'about.html')


def about_company(request):
    return render(request, 'about_company.html', {'company_name': 'Simple Complex'})


def board_topics(request, pk):  # url正则中定义了<pk>
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'topics.html', {'board': board})

