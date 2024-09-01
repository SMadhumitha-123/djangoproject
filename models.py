from django.db import models
from django.contrib.auth.models import User  # Import the User model

# Employee model
class Employee(models.Model):
    emp_id = models.CharField(max_length=10,primary_key=True)
    name = models.CharField(max_length=100, default="Unknown")
    department = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return self.name

# UserProfile model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    

    def __str__(self):
        return self.user.username
class Meta:
        db_table = 'employees_employee'