from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members

def index(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('indexE.html')
  context = {
    'mymembers': mymembers,
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