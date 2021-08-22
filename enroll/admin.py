from django.contrib import admin
from .models import Employee
# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','serial_no','date','employee_name','father_name','gender','residence','dob','physical_fitness','descriptive_marks','refusel_of_certificate','certificate_being_revoked','age','telephone','email','factory','department','examination_after_a_period')