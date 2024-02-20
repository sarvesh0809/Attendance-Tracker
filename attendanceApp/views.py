from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.utils import timezone
from .models import Employee,LeaveType,Leave
from datetime import datetime, timedelta
from .models import UserProfile, Department, Designation,UserType

# @login_required(login_url='/pos/login')
def dashboard(request):
    return render(request, 'main/dashboard.html')



from collections import defaultdict

def view_attendance(request):
    selected_month = int(request.GET.get('month', timezone.now().month))
    selected_year = int(request.GET.get('year', timezone.now().year))
    
    month_choices = [(i, timezone.datetime(1900, i, 1).strftime('%B')) for i in range(1, 13)]
    year_choices = range(2020, timezone.now().year + 1)
    
    leaves = Leave.objects.filter(date__year=selected_year, date__month=selected_month)

    # Group leaves by user
    user_leaves = defaultdict(list)
    for leave in leaves:
        user = f"{leave.employee.user.user.first_name} {leave.employee.user.user.last_name}"
        user_leaves[user].append(leave)
    
    context = {
        'user_leaves': user_leaves.items(),
        'month_choices': month_choices,
        'year_choices': year_choices,
        'selected_month': selected_month,
        'selected_year': selected_year
    }
    
    return render(request, 'master/view_attendance.html', context)




def mark_attendance(request):
    employees = Employee.objects.all()
    leave_types = LeaveType.objects.all()
    return render(request, 'main/mark_attendance.html', {'employees': employees, 'leave_types': leave_types})




def save_leave(request):
    if request.method == 'POST' and request.is_ajax():
        # Retrieve form data
        employee_id = request.POST.get('employee_id')
        date_option = request.POST.get('date_option')
        leave_type_id = request.POST.get('leave_type')
        remarks = request.POST.get('remarks')
        
        # Check if user exists
        try:
            user = User.objects.get(username=employee_id)
        except Exception as e:
            return JsonResponse({'success': False, 'message': 'Please enter a valid user name.'})

        if date_option == 'today':
            # Check if leave entry for today already exists
            leave_date = datetime.now().date()
            existing_leave = Leave.objects.filter(employee__user__user__username=employee_id, date=leave_date).first()
            if existing_leave:
                existing_leave.leave_type_id = leave_type_id
                existing_leave.remarks = remarks
                existing_leave.save()
            else:
                leave = Leave(employee__user__user__username=employee_id, date=leave_date, leave_type_id=leave_type_id, remarks=remarks)
                leave.save()
        elif date_option == 'date_range':
            start_date = datetime.strptime(request.POST.get('start_date'), '%Y-%m-%d').date()
            end_date = datetime.strptime(request.POST.get('end_date'), '%Y-%m-%d').date()

            current_date = start_date
            while current_date <= end_date:
                # Check if leave entry for the current date already exists
                existing_leave = Leave.objects.filter(employee__user__user__username=employee_id, date=current_date).first()
                if existing_leave:
                    existing_leave.leave_type_id = leave_type_id
                    existing_leave.remarks = remarks
                    existing_leave.save()
                else:
                    leave = Leave(employee__user__user__username=employee_id, date=current_date, leave_type_id=leave_type_id, remarks=remarks)
                    leave.save()
                current_date += timedelta(days=1)

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})


def create_employee(request):
    if request.method == 'POST':
        # Process the form data
        try:
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_type_id = request.POST.get('user_type')
            department_id = request.POST.get('department')
            designation_id = request.POST.get('designation')
            
            if User.objects.filter(username=username).exists():
                return JsonResponse({'success': False, 'message': 'Username already exists'})
            # Create the User instance
            user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
            
            # Create the UserProfile instance
            user_type = UserType.objects.get(pk=user_type_id)
            user_profile = UserProfile.objects.create(user=user, user_type=user_type)
            
            # Create the Employee instance
            department = Department.objects.get(pk=department_id)
            designation = Designation.objects.get(pk=designation_id)
            employee = Employee.objects.create(user=user_profile, department=department, designation=designation)
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'message': e})
      
    else:
        # Render the form with empty fields
        user_types = UserType.objects.all()
        departments = Department.objects.all()
        designations = Designation.objects.all()
        return render(request, 'main/create_employee.html', {'user_types': user_types, 'departments': departments, 'designations': designations})
