from django.forms import *
from django import forms
from staff.models import *
from .models import *

class add_student_form(Form) :
    name = CharField(required=True, max_length=100)
    email = EmailField(required=True)
    password = CharField(label="Password", required=True)
    conf_password = CharField(required=True, widget=PasswordInput)
    track_id = ChoiceField(label="Track", choices=(("1", "OS"), ("2", "PWD")), required=True)
    sub_id = ChoiceField(label="Supervisor",required=True,choices=[(sub.id,sub.name) for sub in Staff.objects.all()])


class update_student_form(forms.ModelForm) :
    class Meta:
        model=Student
        fields = ['name', 'email', 'password', 'track', 'staffObj']
        labels = {
        'name': 'Name',
        'email': 'Email',
        'password':'Password',
        'track':'Track',
        'staffObj':'Supervisor',
        }
        widgets = {
        'name': forms.TextInput,
        'email': forms.EmailInput,
        'password': forms.PasswordInput,
        'track': forms.Select(choices=(("1", "OS"), ("2", "PWD"))),
        'staffObj': forms.Select(choices=[(sub.id, sub.name ) for sub in Staff.objects.all()]),

        }