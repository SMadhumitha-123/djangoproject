from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['emp_id', 'name', 'department', 'salary', 'mobile']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

def clean_emp_id(self):
        emp_id = self.cleaned_data.get('emp_id')
        if Employee.objects.filter(emp_id=emp_id).exists():
            raise forms.ValidationError("Employee ID already exists.")
        return emp_id
