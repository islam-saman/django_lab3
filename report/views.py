from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
# Create your views here.

def report_home(req):
    if(req.method=='GET'):
        return render(req,'report/report.html')




def list_student(req):
    if(req.method=='GET'):
        res= HttpResponse()
        res['content-type']='text/plain'
        res.write('list student pages works')
        return res
    else:
        return HttpResponse('access denied')


def list_staff(req):
    if(req.method=='GET'):
        res= HttpResponse()
        res['content-type']='text/plain'
        res.write('list staff pages works')
        return res
    else:
        return HttpResponse('access denied')


