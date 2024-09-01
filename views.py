from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import EmployeeForm, LoginForm
from .models import Employee
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import IntegrityError
from django.contrib.auth.models import User

def is_admin(user):
    return user.is_superuser 

def employee_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('employee_list')
    else:
        form = LoginForm()
    return render(request, 'employees/login.html', {'form': form})

@login_required
def employee_list(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login page if not authenticated

    print(f"User: {request.user.username}")
    print(f"Is Superuser: {request.user.is_superuser}")

    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})
@login_required
@user_passes_test(is_admin)
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('employee_list')
            except IntegrityError:
                error_message = "Employee ID already exists. Please use a unique ID."
                return render(request, 'employees/add_employee.html', {'form': form, 'error_message': error_message})
    else:
        form = EmployeeForm()
    return render(request, 'employees/add_employee.html', {'form': form})

# View for deleting an employee (accessible only by admin users)
@login_required
@user_passes_test(is_admin)
def delete_employee(request, emp_id):
    employee = Employee.objects.get(emp_id=emp_id)
    employee.delete()
    return redirect('employee_list')

# View for user logout
def employee_logout(request):
    logout(request)
    return redirect('employee_login')

# View for user sign-up
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('employee_list')  # Redirect to employee list after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/sign_up.html', {'form': form})



