from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Board


def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})


def about(request):
    return render(request, 'about.html')


def board_topics(request, pk):  # url正则中定义了<pk>
    try:
        board = get_object_or_404(Board, pk=pk)
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'topics.html', {'board': board})

