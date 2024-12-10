from django.db import models

# Create your models here.
class employee(models.Model):
    emp_name=models.CharField(max_length=100)
    salary=models.PositiveIntegerField()
    phone=models.PositiveIntegerField()
    designation=models.CharField(max_length=100)
