from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserType(models.Model):
    role = models.CharField(max_length=100)
    permissions = models.TextField()
    def __str__(self):
        return f'{self.role}'

class Department(models.Model):
    name = models.CharField(max_length=100) 
    working_days=models.IntegerField(default=5)
    def __str__(self):
        return f'{self.name}'

class Designation(models.Model):
    name = models.CharField(max_length=100)
    responsibilities = models.TextField(blank=True)
    def __str__(self):
        return f'{self.name}'

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_type = models.ForeignKey(UserType, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'{self.user}-{self.user_type}' 

class Employee(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    designation = models.ForeignKey(Designation, on_delete=models.SET_NULL, null=True)
    salary = models.IntegerField(default=1)
    doj = models.DateField(blank=True,null=True)
    dob = models.DateField(blank=True,null=True)
    def __str__(self):
        return f'{self.user}-{self.department}' 

class LeaveType(models.Model):
    name = models.CharField(max_length=100,blank=True)
    short_name =  models.CharField(max_length=10,blank=True)
    cut_payement = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.name}'

class Leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(blank=True,null=True)
    leave_type = models.ForeignKey(LeaveType, on_delete=models.SET_NULL, null=True)
    remarks = models.TextField(blank=True)
    def __str__(self):
        return f'{self.employee} - {self.leave_type} - {self.date}'


class HolidayList(models.Model):
    date = models.DateField()
    occasion = models.CharField(max_length=100,blank=True)
    remarks = models.TextField(blank=True)
    def __str__(self):
        return f'{self.occasion}'