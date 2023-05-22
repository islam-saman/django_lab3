from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.db import *
from .forms import *
from student.models import Student
from staff.models import Staff

def student_list(req):
    if(req.method=='GET'):
        context={}
        context['students']=Student.objects.all()
        return render(req,'student/students.html', context)
    else:
        return HttpResponse('access denied')


def insert_student(req):
    if(req.method=='GET'):
        context = {}
        add_form = add_student_form()
        context['add_form'] = add_form
        return render(req,'student/insert.html', context)
    else:
        try:
            Student.objects.create(
            name=req.POST['name'],
            email=req.POST['email'],
            track=req.POST['track_id'],
            password=req.POST['password'],
            staffObj=Staff.objects.get(id=req.POST['sub_id']),)

            return HttpResponseRedirect('/student')

        except DatabaseError:
            context={}
            context['insertError']= True
            return render(req,'student/insert.html', context)


def update_student(req, id):
    if(req.method=='GET'):
        context={}
        update_form = update_student_form()
        context['update_form'] = update_form

        # context['stuff']=Staff.objects.all()
        context['student']=Student.objects.get(id=id)
        return render(req,'student/update.html', context)
    else:
        try:
            Student.objects.filter(id=id).update(
                name=req.POST['name'],
                email=req.POST['email'],
                track=req.POST['track'],
                password=req.POST['password'],
                staffObj=Staff.objects.get(id=1)                
            )
            return HttpResponseRedirect('/student')
        
        except DatabaseError:
            context={}
            context['updateError']= True
            return render(req,'student/update.html', context)

def delete_student(req, id):
    if(req.method=='GET'):
        student = Student.objects.filter(id=id).delete()
        return HttpResponseRedirect('/student')


