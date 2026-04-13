# urls.py
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Emp_list, name='home_page'),
    path('update/<int:id>/', views.Employee_update, name='employee_update'),
    path('delete/<int:id>/', views.delete, name='employee_delete'),
]