from django.shortcuts import render

def index(request):
    return render(request, 'services.html')

def service(ourservice):
    return render(ourservice, '')
