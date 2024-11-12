from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def sweetheart(request):
    return render(request, 'main/sweetheart.html')

def test(request):
    return render(request, 'main/test.html')