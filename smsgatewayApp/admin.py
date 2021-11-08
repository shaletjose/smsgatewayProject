from django.contrib import admin
from .models import SMS,StatusLog
# Register your models here.
class SMSAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SMS._meta.get_fields()]
admin.site.register(SMS,SMSAdmin)
class StatusLogAdmin(admin.ModelAdmin):
    list_display = [field.name for field in StatusLog._meta.get_fields()]
admin.site.register(StatusLog,StatusLogAdmin)
