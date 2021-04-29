from django.urls import path
from .views import createTour, listTour, editTour

urlpatterns = [
    path('create/', createTour, name='create'),
    path('list/', listTour, name='list'),
    path('edit/<int:pk>', editTour, name='edit'),
]
