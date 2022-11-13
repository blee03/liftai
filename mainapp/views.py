from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members
from .models import Test

def index(request):
  vectorOutput = Test.objects.all().values()
  template = loader.get_template('indexE.html')
  context = {
    'testArrayHTML': vectorOutput,
  }
  return HttpResponse(template.render(context, request))
  
def add(request):
  template = loader.get_template('addE.html')
  return HttpResponse(template.render({}, request))
  
def addrecord(request):
  eName = request.POST['name']
  eId = request.POST['id']
  eGroup1 = request.POST['g1']
  eGroup2 = request.POST['g2']
  eGroup3 = request.POST['g3']
  eGroup4 = request.POST['g4']
  eGroup5 = request.POST['g5']
  member = Members(name=eName, exerciseId=eId, group1 = eGroup1, group2 = eGroup2, group3 = eGroup3, group4 = eGroup4, group5 = eGroup5)
  member.save()
  return HttpResponseRedirect(reverse('indexE'))

def sendVector(request):
  testArray = Test(vector = "vectorFromRequest")
  delete_everything(testArray)
  #arrayOut = []
  #arrayOut[0] = 1 if request.POST['exercise'] == "0" else 0
  #arrayOut[1] = 1 if request.POST['exercise'] == "1" else 0
  #arrayOut[2] = 1 if request.POST['exercise'] == "2" else 0
  #arrayOut[3] = 1 if request.POST['exercise'] == "3" else 0

  vectorFromRequest = request.POST['exercise'] 
  testArray = Test(vector = vectorFromRequest)
  testArray.save()

  return HttpResponseRedirect(reverse('indexE'))

def delete_everything(self):
  Test.objects.all().delete()

#find the indicies where the user has selected the excersize and return them in vector form
def findones(vector):
    indiciesVector = []
    for i in range(vector.len):
        if (vector[i] ==  1):
            indiciesVector.append(i)
    return indiciesVector
#take the list of selected excersizes and return the first list that matches the criteria
def matchlist(ind, filename):
    thearray = []
    file3 = open(filename, "r")
    thearray = file3.read()
    file3.close()

    for i in range(thearray.len):
        for j in range(ind.len):
            if (thearray[i][j] != 1):
                break
        return thearray[i]
    Exception("unable to find a match for your excersize")

  
  
