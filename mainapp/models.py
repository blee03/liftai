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