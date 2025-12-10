from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
    path('', views.EmployeeListView.as_view(), name='employee-list'),
    path('add/', views.EmployeeCreateView.as_view(), name='employee-add'),
    path('<int:pk>/', views.EmployeeDetailView.as_view(), name='employee-detail'),
    path('<int:pk>/edit/', views.EmployeeUpdateView.as_view(), name='employee-edit'),
    path('<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='employee-delete'),
]
