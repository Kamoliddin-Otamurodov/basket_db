from django.urls import path
from .views import PlayerView , PlayerDetailView , TeamView , TeamDetailView , CoachView , CoachDetailView , CityView , CityDetailView



urlpatterns = [
    path('player/', PlayerView.as_view()),
    path('player/<int:player_id>/', PlayerDetailView.as_view()),
    path('player/', TeamView.as_view()),
    path('player/<int:player_id>/', TeamDetailView.as_view()),
    path('player/', CoachView.as_view()),
    path('player/<int:player_id>/', CoachDetailView.as_view()),
    path('player/', CityView.as_view()),
    path('player/<int:player_id>/', CityDetailView.as_view()),
    path('player/<int:player_id>/tasks/', CityView.as_view()),
    path('player/<int:player_id>/tasks/<int:task_id>/', CityDetailView.as_view()),
    path('player/<int:player_id>/tasks/', TeamView.as_view()),
    path('player/<int:player_id>/tasks/<int:task_id>/', TeamDetailView.as_view()),
    path('player/<int:player_id>/tasks/', CoachView.as_view()),
    path('player/<int:player_id>/tasks/<int:task_id>/', CoachDetailView.as_view()),
]
