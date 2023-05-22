from django.urls import path
from .views import *
urlpatterns=[
    path('', student_list),
    path('insert/', insert_student, name='add-student'),
    path('update/<int:id>', update_student, name='update-student'),
    path('delete/<int:id>', delete_student, name='delete-student'),
]