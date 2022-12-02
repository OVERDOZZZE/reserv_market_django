from django.shortcuts import render
from .models import Articles
# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def articles(request):
    articles = Articles.objects.all()
    return render(request, 'main/articles.html', {'articles': articles})

