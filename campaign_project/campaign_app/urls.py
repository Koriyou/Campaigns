from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Campaign1.html', views.campaign1, name='campaign1'),
    # Add more URL patterns as needed
]
