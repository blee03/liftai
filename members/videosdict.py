#place to pull the video URLs from

uexcer1 = https://www.youtube.com/embed/vK0haV9km24 #flat_bench
uexcer2 = https://www.youtube.com/embed/tkp22GWXAMI #overhead_press
uexcer3 = https://www.youtube.com/embed/ERXQ3TFPBmI #bent_over_rows
uexcer4 = https://www.youtube.com/embed/PEbucj4fqhE #standard_curls
uexcer5 = https://www.youtube.com/embed/0irSr7p0JdY #tricep_pushdowns
uexcer6 = np.array([1,0,0,0,0]) #chest_fly
uexcer7 = np.array([0,0.95,0,.4,0]) #lat_pulldowns
uexcer8 = np.array([0,0,0,0.9,0]) #preacher_curls
uexcer9 = np.array([0,0.15,1,0,0]) #lat_fly
uexcer10 = np.array([0.8,0,0.7,0,0.7]) #incline_bench
uexcer11 = np.array([0,0.6,0.7,0,0]) #rear_delt_fly
uexcer12 = np.array([0.9,0,0.1,0,0.2]) #chest_press
uexcer13 = https://www.youtube.com/embed/fO82H3F0rw4 #reverse_curls
uexcer14 = https://www.youtube.com/embed/mEbC-y4hs9Q #hammer_curls
uexcer15 = np.array([0,0.85,0,0.7,0]) #dumbell_row
uexcer16 = np.array([0,0.95,0,0.5,0]) #horizontal_cable_pull

lexcer1 = https://www.youtube.com/embed/siIGhA0r4us #dead_lift
lexcer2 = https://www.youtube.com/embed/9GxQ96tlZns #squat
lexcer3 = https://www.youtube.com/embed/ySAA8Ja01hM #lunges
lexcer4 = https://www.youtube.com/embed/WG_g-X-ss98 #abductor
lexcer5 = np.array([0,0.1,0.2,0,0]) #adductor
lexcer6 = https://www.youtube.com/embed/Lz1Oy2i6-Go #calve_machine
lexcer7 = np.array([0,1,0,0,0]) #leg_extensions
lexcer8 = np.array([0,0,0,0,1]) #leg_curls
lexcer9 = np.array([0,0,0.8,0,0.7]) #kickbacks
lexcer10 = https://www.youtube.com/embed/nvwT_X5C_38 #leg_press
lexcer11 = https://www.youtube.com/embed/WNfmSUKg2Rs #cable_squat
lexcer12 = np.array([0.8,0,0.1,0,0]) #band_abduction
lexcer13 = np.array([0.9,0,0.1,0,0]) #seated_band_abduction
lexcer14 = np.array([0,0,0.8,0.05,0.1]) #romanian_deadlift
lexcer15 = np.array([0,0,1,0.1,0.7]) #hip_thrust
lexcer16 = https://www.youtube.com/embed/thGKGVXQdUE #single_leg_squat



#the array containing the coefficents of how many of each excercise to do for arms
Aexcer = np.array([uexcer1,uexcer2,uexcer3,uexcer4,uexcer5,uexcer6,
uexcer7,uexcer8,uexcer9,uexcer10,uexcer11,uexcer12,
uexcer13,uexcer14,uexcer15,uexcer16 ])
#the array containing the coefficents of how many of each excercise to do for legs
Lexcer = np.array([lexcer1,lexcer2,lexcer3,lexcer4,lexcer5,lexcer6,
lexcer7,lexcer8,lexcer9,lexcer10,lexcer11,lexcer12,
lexcer13,lexcer14,lexcer15,lexcer16 ])