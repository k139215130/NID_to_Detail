from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'index.html', {})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
        else:
            return render(request, 'registration/register.html', {'form':form})
    form = UserCreationForm()
    return render(request, 'registration/register.html', {'form':form})