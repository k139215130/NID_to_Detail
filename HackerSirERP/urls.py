"""HackerSirERP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', include('chart.urls')),
    path('', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', views.index, name='index')
]

"""
Error
"""
def handler400(request, exception):
    return render(request, 'error/400.html', status=400)
def handler403(request, exception):
    return render(request, 'error/403.html', status=403)
def handler404(request, exception):
    return render(request, 'error/404.html', status=404)
def handler500(request):
    return render(request, 'error/500.html', status=500)