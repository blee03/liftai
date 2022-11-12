import tensorflow_datasets as tfds
import tensorflow_recommenders as tfrs
import tensorflow as tf
from numpy import array
from manage import *
#UpperBodyMuscleGroups [Pec,Traps, Delts, Bicep, Forearm]
#LowerBodyMuscleGroups [adductor,quadracep, glutes, calves, hammies]

#somehow import the excercise vectors into here
uexcer1 = 0
uexcer2 = 0
uexcer3 = 0
uexcer4 = 0 
uexcer5 = 0
uexcer6 = 0
uexcer7 = 0
uexcer8 = 0
uexcer9 = 0 
uexcer10 = 0
uexcer11 = 0
uexcer12= 0
uexcer13= 0
uexcer14= 0 
uexcer15= 0
uexcer16= 0
lexcer1 = 0
lexcer2 = 0
lexcer3 = 0
lexcer4 = 0 
lexcer5 = 0
lexcer6 = 0
lexcer7 = 0
lexcer8 = 0
lexcer9 = 0 
lexcer10 = 0
lexcer11 = 0
lexcer12= 0
lexcer13= 0
lexcer14= 0 
lexcer15= 0
lexcer16= 0
Acoefficients = array([uexcer1,uexcer2,uexcer3,uexcer4,uexcer5,uexcer6,
uexcer7,uexcer8,uexcer9,uexcer10,uexcer11,uexcer12,
uexcer13,uexcer14,uexcer15,uexcer16 ])

Lcoefficients = array([lexcer1,lexcer2,lexcer3,lexcer4,lexcer5,lexcer6,
lexcer7,lexcer8,lexcer9,lexcer10,lexcer11,lexcer12,
lexcer13,lexcer14,lexcer15,lexcer16 ])