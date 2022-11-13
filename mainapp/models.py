from django.db import models

class Members(models.Model):
  name = models.CharField(max_length=255)
  exerciseId = models.IntegerField()
  group1 = models.DecimalField(max_digits=2, decimal_places=2)
  group2 = models.DecimalField(max_digits=2, decimal_places=2)
  group3 = models.DecimalField(max_digits=2, decimal_places=2)
  group4 = models.DecimalField(max_digits=2, decimal_places=2)
  group5 = models.DecimalField(max_digits=2, decimal_places=2)

class Test(models.Model):
  vector = models.CharField(max_length=69)

class Input(models.Model):
  e0 = models.IntegerField()
  e1 = models.IntegerField()
  e2 = models.IntegerField()
  e3 = models.IntegerField()
  e4 = models.IntegerField()
  e5 = models.IntegerField()
  e6 = models.IntegerField()
  e7 = models.IntegerField()
  e8 = models.IntegerField()
  e9 = models.IntegerField()
  e10 = models.IntegerField()
  e11 = models.IntegerField()
  e12 = models.IntegerField()
  e13 = models.IntegerField()
  e14 = models.IntegerField()
  e15 = models.IntegerField()
