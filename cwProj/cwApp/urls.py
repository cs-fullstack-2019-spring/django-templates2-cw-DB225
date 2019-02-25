from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.index, name="index"),
    path('movies/details/<int:movie_id>/', views.details, name="details"),
    path('movies/synopsis/<int:movie_id>/', views.synopsis, name="synopsis"),
]