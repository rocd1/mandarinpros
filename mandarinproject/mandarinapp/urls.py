from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
     path('lesson/<int:lesson_id>/flashcards/', views.flashcards, name='flashcards'),
]