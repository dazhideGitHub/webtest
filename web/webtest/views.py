from django.shortcuts import render


def index(request):
    return render(request, 'webtest/index.html')
