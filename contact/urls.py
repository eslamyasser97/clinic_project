from django.urls import path
from . import views

appname = 'contact'
urlpatterns = [

path('', views.send_message, name='contact'),



]