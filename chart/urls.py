from django.urls import path

from . import views

urlpatterns = [
    path('single', views.single, name='single'),
    path('multi', views.multi, name='multi'),
    path('edit', views.edit, name='edit'),
    path('chart', views.chart, name='chart')
]