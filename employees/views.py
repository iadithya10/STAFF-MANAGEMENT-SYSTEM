from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Employee
from .forms import EmployeeForm
from django.db.models import Q

class EmployeeListView(ListView):
    model = Employee
    template_name = 'employees/employee_list.html'
    context_object_name = 'employees'
    paginate_by = 12

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q', '').strip()
        dept = self.request.GET.get('department', '')
        status = self.request.GET.get('status', '')
        sort = self.request.GET.get('sort', '')

        if q:
            qs = qs.filter(
                Q(first_name__icontains=q) |
                Q(last_name__icontains=q) |
                Q(email__icontains=q) |
                Q(role__icontains=q)
            )
        if dept:
            qs = qs.filter(department=dept)
        if status:
            if status == 'active':
                qs = qs.filter(is_active=True)
            elif status == 'inactive':
                qs = qs.filter(is_active=False)
        if sort == 'date_asc':
            qs = qs.order_by('date_joined')
        elif sort == 'date_desc':
            qs = qs.order_by('-date_joined')

        return qs

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employees/employee_detail.html'
    context_object_name = 'employee'

class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employees/employee_form.html'

class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employees/employee_form.html'

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employees/employee_confirm_delete.html'
    success_url = reverse_lazy('employees:employee-list')
