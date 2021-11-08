from __future__ import  absolute_import,unicode_literals
from celery import shared_task

from .models import StatusLog
import requests
import json

@shared_task
def schedule2():
    print("hello")
    sms_status=list(StatusLog.objects.filter(updated="false").values())
    print(sms_status)
    # print(list(sms_status.values('messageid','status')))
    payload = {'status':sms_status}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    url = "http://127.0.0.1:8000/smsDeliveryStatus/"
    requests.post(url, data=json.dumps(payload), headers=headers)
    # StatusLog.objects.filter(updated="false").update(updated="true")

   
    