from django.urls import path
from movies.views import MoviesApi, MoviesIdAPi, MovieOrderApi

urlpatterns = [
    path("movies/", MoviesApi.as_view()),
    path("movies/<int:id>/", MoviesIdAPi.as_view()),
    path("movies/<int:id>/orders/", MovieOrderApi.as_view()),
]
