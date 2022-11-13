from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('legs/', views.legs, name='legs'),
  path('arms/', views.arms, name='arms'),
  path('arms/sendExerciseArms/', views.sendExerciseArms, name='sendExerciseArms'),
  path('legs/sendExerciseLegs/', views.sendExerciseLegs, name='sendExerciseLegs'),
  path('arms/sendExerciseArms/results', views.results, name='results'),
  path('legs/sendExerciseLegs/results', views.results, name='results'),
]
