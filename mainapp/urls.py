from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='indexE'),
  path('add/', views.add, name='addE'),
  path('add/sendExercise/', views.sendExercise, name='sendExercise'),
]
