# models.py
from django.db import models

class Employee(models.Model):
    emp_name = models.CharField(max_length=100)
    emp_id = models.IntegerField()
    emp_age = models.IntegerField()
    emp_salary = models.FloatField()
    emp_mobile = models.CharField(max_length=10)

    def __str__(self):
        return self.emp_name