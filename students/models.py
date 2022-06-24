from django.db import models

# Create your models here.
class Student(models.Model):
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female")
    ]
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=64, unique=True)
    phone_no = models.CharField(max_length=10, blank=False)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    dob = models.DateField()
    address = models.TextField(max_length=120)
    department = models.ManyToManyField('Department')

class Department(models.Model):
    department_name = models.CharField(max_length=30)
