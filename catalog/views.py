from django.shortcuts import render

# Create your views here.


def home(request):
    if request.method == 'GET':
        return render(request, 'catalog/home.html')


def contacts(request) -> object:
    if request.method == 'GET':
        return render(request, 'catalog/contacts.html')
