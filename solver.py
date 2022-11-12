import tensorflow_datasets as tfds
import tensorflow_recommenders as tfrs
import tensorflow as tf
import numpy as np
from manage import *
#UpperBodyMuscleGroups [Pec,Traps, Delts, Bicep, Forearm]
#LowerBodyMuscleGroups [adductor,quadracep, glutes, calves, hammies]
    
#somehow import the excercise vectors into here
uexcer1 = np.array([.5,.5,.5,.5,.1]) #benchpress
uexcer2 = np.array([.5,.5,.5,.5,.1]) #benchpress
uexcer3 = np.array([.5,.5,.5,.5,.1]) #benchpress
uexcer4 = np.array([.5,.5,.5,.5,.1]) #benchpress
uexcer5 = np.array([.5,.5,.5,.5,.1]) #benchpress
uexcer6 = np.array([.5,.5,.5,.5,.1]) #benchpress
uexcer7 = np.array([.5,.5,.5,.5,.1]) #benchpress
uexcer8 = np.array([.5,.5,.5,.5,.1]) #benchpress
uexcer9 = np.array([.5,.5,.5,.5,.1]) #benchpress
uexcer10 = np.array([.5,.5,.5,.5,.1]) #benchpress
uexcer11 = np.array([.5,.5,.5,.5,.1]) #benchpress
uexcer12 = np.array([.5,.5,.5,.5,.1]) #benchpress
uexcer13 = np.array([.5,.5,.5,.5,.1]) #benchpress
uexcer14 = np.array([.5,.5,.5,.5,.1]) #benchpress
uexcer15 = np.array([.5,.5,.5,.5,.1]) #benchpress
uexcer16 = np.array([.5,.5,.5,.5,.1]) #benchpress

lexcer1 = np.array([.5,.5,.5,.5,.1]) #benchpress
lexcer2 = np.array([.5,.5,.5,.5,.1]) #benchpress
lexcer3 = np.array([.5,.5,.5,.5,.1]) #benchpress
lexcer4 = np.array([.5,.5,.5,.5,.1]) #benchpress
lexcer5 = np.array([.5,.5,.5,.5,.1]) #benchpress
lexcer6 = np.array([.5,.5,.5,.5,.1]) #benchpress
lexcer7 = np.array([.5,.5,.5,.5,.1]) #benchpress
lexcer8 = np.array([.5,.5,.5,.5,.1]) #benchpress
lexcer9 = np.array([.5,.5,.5,.5,.1]) #benchpress
lexcer10 = np.array([.5,.5,.5,.5,.1]) #benchpress
lexcer11 = np.array([.5,.5,.5,.5,.1]) #benchpress
lexcer12 = np.array([.5,.5,.5,.5,.1]) #benchpress
lexcer13 = np.array([.5,.5,.5,.5,.1]) #benchpress
lexcer14 = np.array([.5,.5,.5,.5,.1]) #benchpress
lexcer15 = np.array([.5,.5,.5,.5,.1]) #benchpress
lexcer16 = np.array([.5,.5,.5,.5,.1]) #benchpress



#the array containing the coefficents of how many of each excercise to do for arms
Aexcer = np.array([uexcer1,uexcer2,uexcer3,uexcer4,uexcer5,uexcer6,
uexcer7,uexcer8,uexcer9,uexcer10,uexcer11,uexcer12,
uexcer13,uexcer14,uexcer15,uexcer16 ])
#the array containing the coefficents of how many of each excercise to do for legs
Lexcer = np.array([lexcer1,lexcer2,lexcer3,lexcer4,lexcer5,lexcer6,
lexcer7,lexcer8,lexcer9,lexcer10,lexcer11,lexcer12,
lexcer13,lexcer14,lexcer15,lexcer16 ])

#just trying shit I will not lie
def computeCombo(Aexcer):
    