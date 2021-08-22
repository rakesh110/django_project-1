from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Employee(models.Model):
    serial_no=models.IntegerField(unique=True)
    date = models.DateTimeField(default=timezone.now)
    employee_name=models.CharField(max_length=80)
    father_name=models.CharField(max_length=80)
    gender = models.CharField(max_length=100)
    residence=models.CharField(max_length=200)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    physical_fitness=models.CharField(max_length=200)
    descriptive_marks=models.CharField(max_length=100)
    refusel_of_certificate=models.CharField(max_length=80)
    certificate_being_revoked=models.CharField(max_length=100)
    age=models.IntegerField()
    telephone = models.PositiveIntegerField(unique=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    factory=models.CharField(max_length=200)
    department=models.CharField(max_length=200)
    examination_after_a_period=models.IntegerField(default=180) 
    
    def __str__(self):
        return self.employee_name
