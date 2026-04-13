# forms.py
from django import forms
from app1.models import Employee


class Employee_form(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class Employee_delete(forms.Form):
    username = forms.CharField(max_length=10)
    password = forms.CharField(
        max_length=10)