from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('legs/', views.legs, name='legs'),
  path('arms/', views.arms, name='arms'),
  path('arms/sendExercise/', views.sendExercise, name='sendExercise'),
  path('legs/sendExercise/', views.sendExercise, name='sendExercise'),
  path('arms/sendExercise/results', views.results, name='results'),
  path('legs/sendExercise/results', views.results, name='results'),
]
