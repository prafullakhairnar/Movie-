from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, MovieRatingsListView

router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movie')

urlpatterns = [
    path('', include(router.urls)),
    path('movies/<int:pk>/ratings/', MovieRatingsListView.as_view(), name='movie-ratings'),
]
