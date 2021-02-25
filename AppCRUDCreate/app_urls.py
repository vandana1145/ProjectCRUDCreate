from django.urls import include, path

from .views import createStudent, viewStudents, updateStudent, deleteStudent, login, logout, createUser, viewUser, updateUser

urlpatterns = [
    # For Student model : to create, view, update, and delete
    path('create/', createStudent, name='create'),
    path('view/', viewStudents, name='view'),
    path('update/<int:id>/', updateStudent, name='update'),
    path('delete/<int:id>/', deleteStudent, name='delete'),

    # For login and logout with authenticated user : Superuser
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),

    # As home page
    path('', viewStudents),

    # For User mode : to create, view, update
    path('createuser/', createUser, name='createuser'),
    path('viewuser/', viewUser, name='viewuser'),
    path('updateuser/', updateUser, name='updateuser')
]