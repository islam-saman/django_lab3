from django.urls import path
from .views import *
urlpatterns=[
    path('', staff_list),
    path('insert/', insert_staff, name='add-staff'),
    path('update/<int:id>', update_staff, name='update-staff'),
    path('delete/<int:id>', delete_staff, name='delete-staff'),
]