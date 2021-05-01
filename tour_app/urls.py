from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import createTour, editTour, searchTour, ListTourView, CreateUserView


router = DefaultRouter()

router.register('list', ListTourView)
router.register('signup', CreateUserView)


urlpatterns = [
    path('create/', createTour, name='create'),
    # path('list/', listTour, name='list'),
    path('edit/<int:pk>', editTour, name='edit'),
    path('search/', searchTour, name='search'),
    # path('signup/', createUser, name='create-user'),

]

urlpatterns += router.urls
