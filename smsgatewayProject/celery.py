from __future__ import absolute_import, unicode_literals
from celery import Celery
from datetime import datetime, timedelta
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smsgatewayProject.settings')
app = Celery('smsgatewayProject')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.beat_schedule = {
    'add-every-10-seconds': {
        'task': 'smsgatewayApp.tasks.schedule2',
        'schedule': 10.0,
    }
}
app.conf.timezone = 'UTC'
app.autodiscover_tasks()
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


# from __future__ import  absolute_import,unicode_literals
# import os

# import smsgatewayApp.views
# from celery import Celery
# from django.conf import settings

# os.environ.setdefault('DJANGO_SETTINGS_MODULE','smsgatewayProject.settings')
# # settings.configure()
# app = Celery('smsgatewayProject')
# app.conf.enable_utc=False
# app.conf.update(timezone='Asia/Kolkata')


# # app.config_from_object('django.conf:settings', namespace='CELERY')
# app.config_from_object(settings, namespace='CELERY')
# # app.conf.beat_schedule={
# #     'every_10s':{
# #         'task':'smsgatewayApp.tasks.schedule1',
# #         'schedule':30,
# #     }
# # }

# # Load task modules from all registered Django apps.
# app.autodiscover_tasks()


# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')
