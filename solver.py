import numpy as np
#UpperBodyMuscleGroups [Pec,Traps, Delts, Bicep, Forearm]
#LowerBodyMuscleGroups [adductor,quadracep, glutes, calves, hammies]
iters = 70000 #because there are about 65 thousand possible combinations (2^16), we should randomize about this many times
Uworkingsolutions = []
Lworkingsolutions = []

uexcer1 = np.array([0.95,0,0.1,0,0.7]) #flat_bench
uexcer2 = np.array([0.2,0,0.8,0,0.7]) #overhead_press
uexcer3 = np.array([0,1,0,0.75,0]) #bent_over_rows
uexcer4 = np.array([0,0,0,1,0]) #standard_curls
uexcer5 = np.array([0,0,0,0,1]) #tricep_pushdowns
uexcer6 = np.array([1,0,0,0,0]) #chest_fly
uexcer7 = np.array([0,0.95,0,.4,0]) #lat_pulldowns
uexcer8 = np.array([0,0,0,0.9,0]) #preacher_curls
uexcer9 = np.array([0,0.15,1,0,0]) #lat_fly
uexcer10 = np.array([0.8,0,0.7,0,0.7]) #incline_bench
uexcer11 = np.array([0,0.6,0.7,0,0]) #rear_delt_fly
uexcer12 = np.array([0.9,0,0.1,0,0.2]) #chest_press
uexcer13 = np.array([0,0,0,0.8,0]) #reverse_curls
uexcer14 = np.array([0,0,0,0.9,0]) #hammer_curls
uexcer15 = np.array([0,0.85,0,0.7,0]) #dumbell_row
uexcer16 = np.array([0,0.95,0,0.5,0]) #horizontal_cable_pull

lexcer1 = np.array([0,0.5,0.7,0,0.6]) #dead_lift
lexcer2 = np.array([0,0.9,0.7,0.1,0.2]) #squat
lexcer3 = np.array([0,0.2,0.3,0.2,0.4]) #lunges
lexcer4 = np.array([0.95,0,0,0,0]) #abductor
lexcer5 = np.array([0,0.1,0.2,0,0]) #adductor
lexcer6 = np.array([0,0,0,1,0]) #calve_machine
lexcer7 = np.array([0,1,0,0,0]) #leg_extensions
lexcer8 = np.array([0,0,0,0,1]) #leg_curls
lexcer9 = np.array([0,0,0.8,0,0.7]) #kickbacks
lexcer10 = np.array([0,0.7,0.6,0,0.4]) #leg_press
lexcer11 = np.array([0,0.7,0.3,0.1,0.3]) #cable_squat
lexcer12 = np.array([0.8,0,0.1,0,0]) #band_abduction
lexcer13 = np.array([0.9,0,0.1,0,0]) #seated_band_abduction
lexcer14 = np.array([0,0,0.8,0.05,0.1]) #romanian_deadlift
lexcer15 = np.array([0,0,1,0.1,0.7]) #hip_thrust
lexcer16 = np.array([0,0.8,0.1,0.1,0.3]) #single_leg_squat



#the array containing the coefficents of how many of each excercise to do for arms
Aexcer = np.array([uexcer1,uexcer2,uexcer3,uexcer4,uexcer5,uexcer6,
uexcer7,uexcer8,uexcer9,uexcer10,uexcer11,uexcer12,
uexcer13,uexcer14,uexcer15,uexcer16 ])
#the array containing the coefficents of how many of each excercise to do for legs
Lexcer = np.array([lexcer1,lexcer2,lexcer3,lexcer4,lexcer5,lexcer6,
lexcer7,lexcer8,lexcer9,lexcer10,lexcer11,lexcer12,
lexcer13,lexcer14,lexcer15,lexcer16 ])

#compute a list of valid linear combinations within a listed tolerance
def computeCombo(Aexcer, solutionSet):
    tolerance = 0.35 # 10% allowable tolerance
    result = [0,0,0,0,0]
    c = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(16):
        c[i] = np.random.randint(0,2)
        result += Aexcer[i]*c[i]
    if (result[0] < 1+tolerance and result[0] >  1-tolerance):
        if (result[1] < 1+tolerance and result[1]> 1-tolerance):
            if (result[2] < 1+tolerance and result[2] > 1-tolerance):
                if (result[3] < 1+tolerance and result[3] > 1-tolerance):
                    if (result[4] < 1+tolerance and result[4] > 1-tolerance):
                            solutionSet.append(c)
    return solutionSet
for upperbodyiterations in  range(iters):
    Uworkingsolutions = computeCombo(Aexcer,Uworkingsolutions)
for lowerbodyiterations in  range(iters):
    Lworkingsolutions = computeCombo(Lexcer,Lworkingsolutions)


file = open("arms.txt", "w+")
for outer in range(len(Uworkingsolutions)):
    for inner in range(16):
        file.write(str(Uworkingsolutions[outer][inner]))
        file.write(" ")
    file.write("\n")
file.close()

file2 = open("legs.txt", "w+")
for outer2 in range(len(Lworkingsolutions)):
    for inner2 in range(16):
        file2.write(str(Lworkingsolutions[outer2][inner2]))
        file2.write(" ")
    file2.write("\n")
file2.close()