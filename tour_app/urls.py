from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import createTour, editTour, searchTour, ListTourView

router = DefaultRouter()

router.register('list', ListTourView)

urlpatterns = [
    path('create/', createTour, name='create'),
    # path('list/', listTour, name='list'),
    path('edit/<int:pk>', editTour, name='edit'),
    path('search/', searchTour, name='search'),
]

urlpatterns += router.urls
