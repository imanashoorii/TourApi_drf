from django.urls import path
from .views import createTour, listTour, editTour, searchTour

urlpatterns = [
    path('create/', createTour, name='create'),
    path('list/', listTour, name='list'),
    path('edit/<int:pk>', editTour, name='edit'),
    path('search/', searchTour, name='search'),
]
