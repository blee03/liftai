from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Input
from .models import Exercise
from .models import Website

import numpy as np

#pushes object to webpage
def results(request):
  testWebsite = Website.objects.all().values()
  template = loader.get_template('results.html')
  context = {
    'htmlOutput': testWebsite,
  }
  return HttpResponse(template.render(context, request))

#display add page
def arms(request):
  template = loader.get_template('arms.html')
  return HttpResponse(template.render({}, request))

def legs(request):
  template = loader.get_template('legs.html')
  return HttpResponse(template.render({}, request))

def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render({}, request))

#delete everything in a model
def delete_everything(self):
  self.objects.all().delete()

#recieve exersize from user input and place into list for processing
def sendExerciseArms(request):
  armExcer = ("Flat Bench", "Overhead Press", "Bent Over Rows", "Standard Curls",
"Tricep Pushdown", "Chest Fly", "Lat Pulldown" , "Preacher Curl", "Lat Fly",
"Incline Bench", "Rear Delt Fly", "Chest Press", "Reverse Curls", "Hammer Curl",
"Dumbell Row", "Horizontal Cable Pull")

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

  arrayOut = []
  arrayOut.append(1) if request.POST['arms'] == "exercise0" else arrayOut.append(0)
  arrayOut.append(1) if request.POST['arms'] == "exercise1" else arrayOut.append(0)
  arrayOut.append(1) if request.POST['arms'] == "exercise2" else arrayOut.append(0)
  arrayOut.append(1) if request.POST['arms'] == "exercise3" else arrayOut.append(0)
  arrayOut.append(1) if request.POST['arms'] == "exercise4" else arrayOut.append(0)
  arrayOut.append(1) if request.POST['arms'] == "exercise5" else arrayOut.append(0)
  arrayOut.append(1) if request.POST['arms'] == "exercise6" else arrayOut.append(0)
  arrayOut.append(1) if request.POST['arms'] == "exercise7" else arrayOut.append(0)
  arrayOut.append(1) if request.POST['arms'] == "exercise8" else arrayOut.append(0)
  arrayOut.append(1) if request.POST['arms'] == "exercise9" else arrayOut.append(0)
  arrayOut.append(1) if request.POST['arms'] == "exercise10" else arrayOut.append(0)
  arrayOut.append(1) if request.POST['arms'] == "exercise11" else arrayOut.append(0)
  arrayOut.append(1) if request.POST['arms'] == "exercise12" else arrayOut.append(0)
  arrayOut.append(1) if request.POST['arms'] == "exercise13" else arrayOut.append(0)
  arrayOut.append(1) if request.POST['arms'] == "exercise14" else arrayOut.append(0)
  arrayOut.append(1) if request.POST['arms'] == "exercise15" else arrayOut.append(0) 


  # testExercises = Exercise(0)
  # delete_everything(Exercise)

  foundExercises = findones(arrayOut)

  # testExercises = Exercise(eId=foundExercises[0])
  # testExercises.save()

  found = matchlist(foundExercises, "mainapp/arms.txt")

  testInput = Input(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
  delete_everything(Input)

  testInput = Input(
  e0 = found[0], 
  e1 = found[1], 
  e2 = found[2],
  e3 = found[3], 
  e4 = found[4], 
  e5 = found[5], 
  e6 = found[6], 
  e7 = found[7], 
  e8 = found[8], 
  e9 = found[9], 
  e10 = found[10], 
  e11 = found[11], 
  e12 = found[12], 
  e13 = found[13], 
  e14 = found[14], 
  e15 = found[15], 
  ) 
  testInput.save()

  exersizes = findones(found)

  testWebsite = Website(name = "temp", description = "temp", link = "temp")
  delete_everything(Website)

  for i in range(len(exersizes)):
    testWebsite = Website(name = armExcer[exersizes[i]], description = armDescrip[exersizes[i]], link = "temp")
    testWebsite.save()

  return HttpResponseRedirect('results')  

def sendExerciseLegs(request):
  legExcer = ("Dead Lift", "Squat" , "Lunges", "Abductor", "Adductor", "Calf Machines",
"Leg Extensions", "Leg Curls", "Kickbacks", "Leg Press", "Cable Squat", "Band Abduction",
"Seated Band Abduction", "Romanian Deadlift", "Hip Thrust", "Single Leg Squat")

  legDescrip = ("Start with the bar fully at rest on the floor or on guards, \ngrip the bar at shoulder width and lift with your legs until the bar is locked at hip level. Carefully return the bar to the floor and make sure to maintain a straight back"
,"Start with the bar at about shoulder level, step under and lift it with your legs. Step backwards and squat down until your hip is in line with your knee. Stand up and repeat.",
"Using dumbells or unweighted, extend your foot forward until your quadricep is parallel with the ground. Continue for as many reps as you like",
"Place your knees firmly against the guides, and press outward with a full range of motion, control the negative and repeat",
"Place your knees firmly against the guides, and press inward until the knee guards touch",
"With the front of your feet on the foothold, slowly push back and forth with your ankle, making sure to minimize leg movement",
 "With the pad low on your shins, extend your legs until straight, and slowly lower them all the way down", 
 "With the pad low on your calves, but not at the ankles, pull the pad as far as your body allows you to and slowly let it back up", 
 "Place one foot on the plate and push making sure to use your hamstring", 
 "Being careful not to fully lock your legs, push the footplate out, and slowly let it come back to the original position", 
 "Hold both cables above the head being sure to minimize arm movement, quickly lower to the ground, and push back up with a straight back", 
 "With the band going from leg to leg, push one leg out as far as your flexibility allows, you should hold onto something for balance", 
 "With a resistance band around the thighs, push your legs out for a full range of motion, and allow them to come back", 
 "Slowly lower the bar until it drops below the knees, make sure to slightly bend the legs", 
 "With weight on the hips, push upwards until straight, then let the weight slowly drop", 
 "With dumbells in both hands, bend one leg until it is nearly parallel with the floor, the other leg will remain on the bench")

  arrayOut = []
  arrayOut.append(1) if request.POST['legs'] == "exercise0" else arrayOut.append(0)
  arrayOut.append(1) if request.POST['legs'] == "exercise1" else arrayOut.append(0)
  arrayOut.append(1) if request.POST['legs'] == "exercise2" else arrayOut.append(0)
  arrayOut.append(1) if request.POST['legs'] == "exercise3" else arrayOut.append(0)
  arrayOut.append(1) if request.POST['legs'] == "exercise4" else arrayOut.append(0)
  arrayOut.append(1) if request.POST['legs'] == "exercise5" else arrayOut.append(0)
  arrayOut.append(1) if request.POST['legs'] == "exercise6" else arrayOut.append(0)
  arrayOut.append(1) if request.POST['legs'] == "exercise7" else arrayOut.append(0)
  arrayOut.append(1) if request.POST['legs'] == "exercise8" else arrayOut.append(0)
  arrayOut.append(1) if request.POST['legs'] == "exercise9" else arrayOut.append(0)
  arrayOut.append(1) if request.POST['legs'] == "exercise10" else arrayOut.append(0)
  arrayOut.append(1) if request.POST['legs'] == "exercise11" else arrayOut.append(0)
  arrayOut.append(1) if request.POST['legs'] == "exercise12" else arrayOut.append(0)
  arrayOut.append(1) if request.POST['legs'] == "exercise13" else arrayOut.append(0)
  arrayOut.append(1) if request.POST['legs'] == "exercise14" else arrayOut.append(0)
  arrayOut.append(1) if request.POST['legs'] == "exercise15" else arrayOut.append(0) 


  # testExercises = Exercise(0)
  # delete_everything(Exercise)

  foundExercises = findones(arrayOut)

  # testExercises = Exercise(eId=foundExercises[0])
  # testExercises.save()

  found = matchlist(foundExercises, "mainapp/legs.txt")

  testInput = Input(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
  delete_everything(Input)

  testInput = Input(
  e0 = found[0], 
  e1 = found[1], 
  e2 = found[2],
  e3 = found[3], 
  e4 = found[4], 
  e5 = found[5], 
  e6 = found[6], 
  e7 = found[7], 
  e8 = found[8], 
  e9 = found[9], 
  e10 = found[10], 
  e11 = found[11], 
  e12 = found[12], 
  e13 = found[13], 
  e14 = found[14], 
  e15 = found[15], 
  ) 
  testInput.save()

  exersizes = findones(found)

  testWebsite = Website(name = "temp", description = "temp", link = "temp")
  delete_everything(Website)

  for i in range(len(exersizes)):
    testWebsite = Website(name = legExcer[exersizes[i]], description = legDescrip[exersizes[i]], link = "temp")
    testWebsite.save()

  return HttpResponseRedirect('results')  

#find the indicies where the user has selected the excersize and return them in vector form
def findones(vector):
    indiciesVector = [] 
    for i in range(len(vector)):
        if (vector[i] ==  1):
            indiciesVector.append(i)
    return indiciesVector

#take the list of selected excersizes and return the first list that matches the criteria
def matchlist(ind, filename):
    indextocheck = ind[0]
    theactualarray = np.loadtxt(filename, dtype=int)
    for i in range(theactualarray.shape[0]):
        if (theactualarray[i][indextocheck] == 1):
            return theactualarray[i]
    Exception("Unable to find a match")