from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='indexE'),
  path('add/', views.add, name='addE'),
  path('add/addrecord/', views.addrecord, name='addrecord'),
  path('add/sendVector/', views.sendVector, name='sendVector'),
  path('add/sendExercise/', views.sendExercise, name='sendExercise'),
]