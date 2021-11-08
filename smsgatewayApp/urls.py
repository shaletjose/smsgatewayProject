from django.urls import path
from smsgatewayApp import views
app_name='smsgatewayApp'
urlpatterns = [
  
    path('',views.smssendAPI,name='smssendAPI'),
    path('smsdisplay/', views.smsDisplay, name='smsdisplay'),
    path('statusUpdate/',views.statusUpdate,name='statusUpdate'),


]