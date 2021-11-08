from __future__ import absolute_import,unicode_literals
import threading
import requests
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json
from celery import Celery
# from celery import task  
from celery import  shared_task

from import_export.formats.base_formats import JSON

from .models import SMS,StatusLog
# celery = Celery('tasks', broker='amqp://guest@localhost//')


@csrf_exempt
# Create your views here.
def smssendAPI(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        messageid = body['id']
        number = body['number']
        message = body['message']
        SMSDb = SMS()
        SMSDb.messageid = messageid
        SMSDb.phone = number
        SMSDb.message = message
        SMSDb.save()
    return redirect('/smssendAPI')


def smsDisplay(request):
    sms_db = SMS.objects.all()
    return render(request, 'displayMessage.html', {'smsdb': sms_db})


def statusUpdate(request):
        print("called-----------")
        id= request.GET.get('id')
        message=request.GET.get('message')
        status1=request.GET.get('status')
        print("id:",id)
        print("message:",message)
        print("status:",status1)
        if ((status1 != "Choose Delivery status")  and (id != "")):
            if(StatusLog.objects.filter(messageid=id).exists()):
                        StatusLog.objects.filter(messageid=id).update(status=status1)
                        messages.info(request,"Status Updated")
            else:
                        statuslog = StatusLog()
                        statuslog.messageid =id
                        statuslog.status =status1
                        statuslog.updated="false"
                        statuslog.save()
            # payload = {'status':status,'id':id}
            # headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            # url = "http://127.0.0.1:8000/smsDeliveryStatus/"
            # requests.post(url, data=json.dumps(payload), headers=headers)
        # schedule1()
        return redirect('smsdisplay/')

# @shared_task
# def schedule1():
#     sms_status = StatusLog.objects.filter(updated="false")
#     print(list(sms_status.values('messageid','status')))
#     payload = {'status':sms_status}
#     headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
#     url = "http://127.0.0.1:8000/smsDeliveryStatus"
#     # requests.post(url, data=json.dumps(payload), headers=headers)
#     StatusLog.objects.filter(updated="false").update(updated="true")

   
  
   



