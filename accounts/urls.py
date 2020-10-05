from django.urls import path
from . import views

appname = 'accounts'
urlpatterns = [
path('signup', views.signup, name='signup'),
path('profile', views.profile, name='profile'),
path('edit/profile', views.edit_profile, name='profile_edit'),

]

