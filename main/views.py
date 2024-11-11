from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('<h4>Перевірка робити сайту</h4>')

def about(request):
    return HttpResponse('<h4>Сторінка про нас</h4>')

def sweetheart(request):
    return HttpResponse('<h1>Люблю тебе)</h1>')

def test(request):
    return HttpResponse('<h4>Тестова сторінка</h4>')