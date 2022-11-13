from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Input
from .models import Exercise

#pushes object to webpage
def results(request):
  testExercises = Exercise.objects.all().values()
  template = loader.get_template('results.html')
  context = {
    'htmlOutput': testExercises,
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
def sendExercise(request):
  arrayOut = []
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
  arrayOut.append(1) if request.POST['arms'] == "exercise16" else arrayOut.append(0)  

  testExercises = Exercise(0)
  delete_everything(Exercise)

  foundExercises = findones(arrayOut)

  testExercises = Exercise(eId=foundExercises[0])
  testExercises.save()

  # #found = matchlist(foundExercises, "arms.txt")

  # #testInput = Input(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
  # #delete_everything(Input)

  # testInput = Input(
  # e0 = found[0], 
  # e1 = found[1], 
  # e2 = found[2],
  # e3 = found[3], 
  # e4 = found[4], 
  # e5 = found[5], 
  # e6 = found[6], 
  # e7 = found[7], 
  # e8 = found[8], 
  # e9 = found[9], 
  # e10 = found[10], 
  # e11 = found[11], 
  # e12 = found[12], 
  # e13 = found[13], 
  # e14 = found[14], 
  # e15 = found[15], 
  # ) 
  # testInput.save()

  return HttpResponseRedirect('results')  

#find the indicies where the user has selected the excersize and return them in vector form
def findones(vector):
    indiciesVector = [] 
    for i in range(len(vector)):
        if (vector[i] ==  1):
            indiciesVector.append(i)
    return indiciesVector
