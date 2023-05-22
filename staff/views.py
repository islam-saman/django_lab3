from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.db import *
from staff.models import Staff

def staff_list(req):
    if(req.method=='GET'):
        context={}
        context['staffs']=Staff.objects.all()
        return render(req,'staff/staff.html',context)
    else:
        return HttpResponse('access denied')


def insert_staff(req):
    if(req.method=='GET'):
        return render(req,'staff/insert.html')
    else:
        try:
            new_staff = Staff.objects.create(
            name=req.POST['name'],
            email=req.POST['email'],
            department=req.POST['department'],
        )
            return HttpResponseRedirect('/staff')

        except DatabaseError:
            return render(req,'staff/insert.html')
            

def update_staff(req, id):
    if(req.method=='GET'):
        context={}
        context['staff']=Staff.objects.get(id=id)
        return render(req,'staff/update.html', context)
    else:
        try:
            Staff.objects.filter(id=id).update(
                name=req.POST['name'],
                email=req.POST['email'],
                department=req.POST['department'],
            )
            return HttpResponseRedirect('/staff')
        
        except DatabaseError:
            context={}
            context['updateError']= True
            return render(req,'staff/update.html', context)

def delete_staff(req, id):
    if(req.method=='GET'):
        staff = Staff.objects.filter(id=id).delete()
        return HttpResponseRedirect('/staff')


