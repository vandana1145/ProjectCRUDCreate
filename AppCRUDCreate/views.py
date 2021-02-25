from django.shortcuts import render, redirect
from .forms import StudentForm, UserForm
from .models import Student, User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

# For Student Model : create views for creating Student, viewing Student, updating student, and deleting Student
def createStudent(req):
    form = StudentForm()
    if req.method == 'POST':
        form = StudentForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, 'Profile has been created.')
            return redirect('view')
      
    context = {
        'name' : ' CRUD ',
        'lang' : 'python',
        # 'form' : {
        #     'name':'django'
        # },
        'form' : form
    }
    return render(req, 'createStudent.html', context)

@login_required(login_url='login')
def viewStudents(req):
    students = Student.objects.all()
    # students = Student.objects.get(id=1)
    print(students)
    return render(req, 'viewStudent.html', { 'students' : students})

@login_required(login_url='login')
def updateStudent(req, id):
    student = Student.objects.get(id=id)
    print(student)
    # form = StudentForm(initial={'fname': student.fname, 'lname': student.lname})
    form = StudentForm(instance=student)
    if req.method == 'POST':
        form = StudentForm(req.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(req, 'Profile has been updated.')
            return redirect('view')
    return render(req, 'updateStudent.html', {'form':form})

def deleteStudent(req, id):
    student = Student.objects.get(id=id)
    student.delete()
    messages.success(req, 'Profile has been deleted.')
    return redirect('view')


from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .decorators import unauthenticated_user


# Create views for autheticated user login and logout
@unauthenticated_user
def login(req):
    username = req.POST.get('username')
    password = req.POST.get('password')
    user = authenticate(req, username=username, password=password)
    if req.POST:
        if user is not None:
            auth_login(req, user)
            return redirect('view')
        messages.error(req, 'Invalid username or password!')
    return render(req, 'login.html')


def logout(req):
    auth_logout(req)
    return redirect('login')
    # return render(req, 'logout.html')


# Create views for User : createUser, viewUser and updateUser
def createUser(req):
    form = UserForm()
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, 'User has been created successfully.')
            return redirect('viewuser')
    
    context = {
        'form' : form
    }
    return render(req, 'createuser', context)


def viewUser(req):
    users = User.objects.all()
    print(users)
    return render(req, 'viewUser.html', {'users': users})


def updateUser(req):
    user = User.objects.get(id=id)
    print (user)
    form = UserForm(instance=user)
    if req.method == 'POST':
        form = UserForm(req.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(req, 'User detail has been updated.')
            return redirect('viewuser')
    return render(req, 'updateUser.html', {'form':form})