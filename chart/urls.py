from django.urls import path

from . import views

urlpatterns = [
    path('single', views.single, name='single'),
    path('multi', views.multi, name='multi'),
    path('chart', views.chart, name='chart'),
    path('bot', views.bot, name='bot'),
]