from django.contrib import admin
from .models import Student, User

# Register your models here.

#Student
admin.site.register(Student)

#User
admin.site.register(User)