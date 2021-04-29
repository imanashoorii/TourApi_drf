from django.urls import path
from .views import createTour

urlpatterns = [
    path('create/', createTour, name='create')
]