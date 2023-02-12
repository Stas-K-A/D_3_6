from django.shortcuts import render
from .models import News


def news_page(request):
    news = News.objects.all().order_by('-date_creation')
    return render(request, 'default.html', context={'news': news})


def detail(request, slug):
    news_detail = News.objects.get(slug__iexact=slug)
    return render(request, 'news_text.html', context={'news_detail': news_detail})


