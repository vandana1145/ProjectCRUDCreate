# import form class from django
from django import forms

# import Student models from models.py
from .models import Student, User
from django.contrib.auth.models import User as AuthUser

from django.forms.widgets import NumberInput

# Django ModelForm - Create form from Models: Django ModelForm is a class that is used to directly convert a model into a Django form. 
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        #exclude =['roll_num']
        widgets = {
            # 'fname': forms.TextInput(attrs={'class':'form-control'}),
            'subject': forms.Textarea(attrs={'class':'form-control'}),
        }

# A widget is Django’s representation of an HTML input element. The widget handles the rendering of the HTML, and the extraction of data from a GET/POST dictionary that corresponds to the widget.
class UserForm(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = "__all__"
        widgets = {
            # CharField() with Textarea widget
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'date_joined': forms.DateInput(attrs={'type': 'date', 'class':'form-control'}),
            'password': forms.TextInput(attrs={'class':'form-control'}),
        }