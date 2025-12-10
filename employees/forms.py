from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name','last_name','email','phone','department','role','address','photo','salary','is_active']
        widgets = {
            'address': forms.Textarea(attrs={'rows':3}),
            'date_joined': forms.DateInput(attrs={'type':'date'}),
        }
