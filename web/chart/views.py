from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def single(request):
    return render(request, 'single.html', {})

def multi(request):
    return render(request, 'multi.html', {})

def chart(request):
    return render(request, 'chart.html', {})

def edit(request):
    return render(request, 'edit.html', {})