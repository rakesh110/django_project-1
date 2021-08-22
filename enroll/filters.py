from .models import Employee
from django_filters import DateFilter, CharFilter
import datetime
import django_filters

class EmployeeFilter(django_filters.FilterSet):
    date=DateFilter(field_name="date" , lookup_expr='gte')
    employee_name=CharFilter(field_name="employee_name",lookup_expr='icontains')
    factory=CharFilter(field_name="factory",lookup_expr='icontains')
    class Meta:
        model = Employee
        fields = ['date', 'employee_name', 'factory', ]