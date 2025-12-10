from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'department', 'role', 'is_active', 'date_joined')
    list_filter = ('department', 'is_active', 'date_joined')
    search_fields = ('first_name', 'last_name', 'email', 'role')
    list_per_page = 25
