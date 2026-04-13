from django.contrib import admin

# Register your models here.
from app1.models import Employee

class Employee_admin(admin.ModelAdmin):
    list_display=['emp_name','emp_id','emp_age','emp_salary','emp_mobile']

admin.site.register(Employee,Employee_admin)