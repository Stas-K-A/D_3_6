from django.urls import path
from .views import news_page, detail

urlpatterns = [
    path('news/', news_page, name='news_page'),
    path('news/<str:slug>', detail, name='detail')
]