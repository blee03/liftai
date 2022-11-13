import numpy as np

#find the indicies where the user has selected the excersize and return them in vector form
def findones(vector):
    indiciesVector = []
    for i in range(len(vector)):
        if (vector[i] ==  1):
            indiciesVector.append(i)
    return indiciesVector
#take the list of selected excersizes and return the first list that matches the criteria
def matchlist(ind, filename):
    outputList = []
    theactualarray = np.loadtxt(filename, dtype=object)
    for i in range(theactualarray.size):
        for j in range(len(ind)):
            if (theactualarray[i][j] != 1):
                break
        return theactualarray[i]
    Exception("Unable to find a match")

vec = [0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0]
vecones = findones(vec)
print(vecones)
vecfound = matchlist(vecones, "legs.txt")
print(vecfound)

armExcer = ("Flat Bench", "Overhead Press", "Bent Over Rows", "Standard Curls",
"Tricep Pushdown", "Chest Fly", "Lat Pulldown" , "Preacher Curl", "Lat Fly",
"Incline Bench", "Rear Delt Fly", "Chest Press", "Reverse Curls", "Hammer Curl"
"Dumbell Row", "Horizontal Cable Pull")

legExcer = ("Dead Lift", "Squat" , "Lunges", "Abductor", "Adductor", "Calf Machines",
"Leg Extesnions", "Leg Curls", "Kickbacks", "Leg Press", "Cable Squat", "Band Abduction",
"Seated Band Abduction", "Romanian Deadlift", "Hip Thrust", "Single Leg Squat")

armDescrip = ("Lay down on the bench, with your feet firmly on the floor and your hands shoulder width apart on the bar. \nPush until you have locked the bar above your head and return the bar to your chest.",
"Can be completed either sitting or standing, take the barbell and lift it above your head until your elbows are locked.\nReturn the bar to your chest, being sure to control the negative.",
"Best completed with guards installed, lean over as far as is comfortable, and use your arms and back to lift the center of the bar to yoru chest. \nReturn to a neutral position and repeat",
"Using dumbells or a curl bar, engage your biceps as you lift the weight to your chest, being sure not to jerk or engage your shoulders.\nReturn to a neutral position and repeat.",
"With your knees slightly bent, pull down on the grip with both hands until they are in line with your pelvis, \nbeing sure to avoid jerking or breaking your back or leg position",
"Press the bars of the machine until you are making a straight line between your arms, control the negative as you return to a neutral position.",
"To engage the pectoral muscles, lean back and pull the bar to your chest, controling the positive and negative",
"Curl the bar as far as you can, maintaining a smooth motion, and gently return the grips to a neutral position.",
"Using dumbells, lift them as high as you can keeping a lateral path, ending up forming a straight line with your arms",
"Sit comfortably on the bench with your feet firmly on the floor, rest the bar on your upper chest \n and raise it until you are locked out, return to your chest and repeat",
"Leaning down as far as is comfortable from a standing position, raise dumbells laterally, \nengaging your back and triceps, returning to a neutral position in front of the body",
"Sitting comfortably at the machine with your feet on the floor, press the bars fully, extending your arms.\nGently return the bar to neutral.",
"Engaging your forarms, lift the bar to  your chest, gripping the bar from above. \nDo not adjust your grip as you complete the motion, allow the bar to rotate.",
"Holding the dumbells perpendicular to the floor, lift them to your chest and return to a neutral position",
"Using a single dumbell, brace yourself against the bench with your hand, and pull the dumbell from the floor to your chest, and return it to a neutral position",
"Sit down on the bench, with your feet on the platforms, and pull the bar to your chest, leaning back slightly.\nReturn the bar to a neutral position")

legDescrip = ("Start with the bar fully at rest on the floor or on guards, \ngrip the bar at shoulder width and lift with your legs until the bar is locked at hip level. Carefully return the bar to the floor"
,"Start with the bar at about shoulder level, step under and lift it with your legs. Step backwards and squat down until your hip is in line with your knee. Stand up and repeat.",
"Using dumbells or unweighted, extend your foot forward until your quadracep is parallel with the ground. Continue for as many reps as you like",
"Place your knees firmly against the guides, and press outward with a full range of motion, control the negative and repeat",
"Place your knees firmly aganst the guides, and press inward until the knee guards touch",
"f")