from django.contrib import admin
from .models import UserType, Department, Designation, UserProfile, Employee, LeaveType, Leave, HolidayList
from django.contrib.auth.models import User
# Define an inline admin for UserProfile


admin.site.register(UserType)
admin.site.register(Department)
admin.site.register(Designation)
admin.site.register(LeaveType)
admin.site.register(UserProfile)
admin.site.register(Employee)
admin.site.register(Leave)
admin.site.register(HolidayList)
