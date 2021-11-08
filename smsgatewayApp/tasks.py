from __future__ import  absolute_import,unicode_literals
from celery import shared_task
from .models import StatusLog

@shared_task
def schedule1():
    sms_status = StatusLog.objects.filter(updated="false")
    print(list(sms_status.values('messageid','status')))
    payload = {'status':sms_status}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    url = "http://127.0.0.1:8000/smsDeliveryStatus"
    # requests.post(url, data=json.dumps(payload), headers=headers)
    StatusLog.objects.filter(updated="false").update(updated="true")