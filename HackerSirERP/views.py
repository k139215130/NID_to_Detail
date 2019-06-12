from django.shortcuts import render

def index(request):
    return(request, 'index.html', {})