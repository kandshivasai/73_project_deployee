# views.py
from django.shortcuts import render, redirect, get_object_or_404
from app1.models import Employee
from app1.forms import Employee_form, Employee_delete
from django.http import HttpResponse


def Emp_list(request):
    data = Employee.objects.all()
    form = Employee_form()

    if request.method == "POST":
        form = Employee_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')

    return render(request, 'Emp_list.html', {'data': data, 'form': form})


def Employee_update(request, id):
    employee = get_object_or_404(Employee, id=id)
    form = Employee_form(instance=employee)

    if request.method == 'POST':
        form = Employee_form(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('home_page')

    return render(request, 'emp_update.html', {'form': form})


def delete(request, id):
    def_username = 'shiva'
    def_password = 'shiva123'

    emp = Employee.objects.get(id=id)
    emp_del = Employee_delete()

    if request.method == 'POST':
        emp_del = Employee_delete(request.POST)

        if emp_del.is_valid():
            user = emp_del.cleaned_data['username']
            password = emp_del.cleaned_data['password']

            if user == def_username and password == def_password:
                emp.delete()
                return redirect('home_page')
            else:
                return HttpResponse('<h1>invalid username/password</h1>')

    return render(request, 'dellete.html', {'emp_del': emp_del})