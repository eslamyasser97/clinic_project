from django.urls import path

from . import views
appname = 'clinics'
urlpatterns = [
path('', views.clinic_list, name='clinic_list'),
##path('clinic_login/' , views.clinic_login, name='clinic_login'),
path('clinic_profile/' , views.clinic_profile, name='clinic_profile'),
path('add_clinic/' , views.add_clinic, name='add_clinic'),
path('apply_done/' , views.clinic_detail, name='apply_done'),
path('<slug:slug>/' , views.clinic_detail, name='clinic_detail'),


]