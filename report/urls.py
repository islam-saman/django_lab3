from django.urls import path
from .views import *
urlpatterns=[
    path('', report_home),
    path('students', list_student),
    path('staff/', list_staff),
]