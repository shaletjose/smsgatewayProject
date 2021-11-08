from django.db import models

# Create your models here.
class SMS(models.Model):
    messageid = models.CharField(max_length=250)
    message = models.CharField(max_length=250)
    phone=models.CharField(max_length=250)
    def __str__(self):
        return self.phone
class StatusLog(models.Model):
    messageid = models.CharField(max_length=250)
    status = models.CharField(max_length=250)
    updated= models.CharField(max_length=250)
    def __str__(self):
        return self.messageid
