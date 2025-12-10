from django.db import models
from django.urls import reverse

class Employee(models.Model):
    DEPARTMENT_CHOICES = [
        ('HR', 'Human Resources'),
        ('ENG', 'Engineering'),
        ('SALES', 'Sales'),
        ('MK', 'Marketing'),
        ('FIN', 'Finance'),
        ('OPS', 'Operations'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    department = models.CharField(max_length=10, choices=DEPARTMENT_CHOICES)
    role = models.CharField(max_length=100)
    date_joined = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    address = models.TextField(blank=True)
    photo = models.ImageField(upload_to='employee_photos/', blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.department})"

    def get_absolute_url(self):
        return reverse('employees:employee-detail', args=[str(self.id)])
